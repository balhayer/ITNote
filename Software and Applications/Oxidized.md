## Installation using docker

### Clone git repo
```bash
git clone https://github.com/ytti/oxidized
```
### Build container locally
```bash
docker build -q -t oxidized:latest oxidized/
```

### Create a configuration directory
```bash
mkdir /etc/oxidized
```

### Run the container for the first time to initialize the config or copy config file over to configuration directory:
```bash
docker run --rm -v /etc/oxidized:/root/.config/oxidized -p 8888:8888/tcp -t oxidized:latest
```

- Create the /etc/oxidized/router.db (see CSV Source for further info)

### Run container again with new configuration
```bash
docker run -v /etc/oxidized:/root/.config/oxidized -p 8888:8888/tcp -t oxidized:latest
```

### Run container with reloaded configuration frequently
```bash
docker run -v /etc/oxidized:/root/.config/oxidized -p 8888:8888/tcp -e CONFIG_RELOAD_INTERVAL=3600 -t oxidized:latest
```

## Some issues

### Container can’t boot due to a server is already running

- Container can’t run due to oxidized | A server is already running. Check /root/.config/oxidized/pid

- Reason: a pid file is existed in oxidized configuration folder

- Temporary Solution: remove pid file and start container again

- Permanent Solution: create a script file to remove pid file before running oxidized and run it as startup script
```bash
/etc/oxidized/startup.sh on host
#!/bin/sh
rm /root/.config/oxidized/pid
oxidized

Then
chmod 755 /etc/oxidized/startup.sh

To run oxidized container with this script
docker run -it --name oxidized -v /etc/oxidized:/root/.config/oxidized -v /etc/localtime:/etc/localtime:ro -p 8888:8888/tcp -t oxidized:latest /root/.config/oxidized/startup.sh
```

## Creating and Extending Model

### Extending model to support CheckPoint Gaia OS SP

- Create a file named: /etc/oxidized/model/gaiossp.rb with content
```bash
class GaiaOSSP < Oxidized::Model
  # CheckPoint - Gaia OS Model

  # Gaia Prompt
  prompt /^([\[.*\]\s\w.@:-]+[#>]\s?)$/

  # Comment tag
  comment  '# '

  cmd :all do |cfg|
    cfg.cut_both
  end

  cmd :secret do |cfg|
    cfg.gsub! /^(set expert-password-hash ).*/, '\1<EXPERT PASSWORD REMOVED>'
    cfg.gsub! /^(set user \S+ password-hash ).*/, '\1<USER PASSWORD REMOVED>'
    cfg.gsub! /^(set ospf .* secret ).*/, '\1<OSPF KEY REMOVED>'
    cfg.gsub! /^(set snmp community )(.*)( read-only.*)/, '\1<SNMP COMMUNITY REMOVED>\3'
    cfg.gsub! /^(add snmp .* community )(.*)(\S?.*)/, '\1<SNMP COMMUNITY REMOVED>\3'
    cfg.gsub! /(auth|privacy)(-pass-phrase-hashed )(\S*)/, '\1-pass-phrase-hashed <SNMP PASS-PHRASE REMOVED>'
    cfg
  end

  cmd 'set clienv rows 0' do |cfg|
    comment cfg
  end

  cmd 'show version all' do |cfg|
    comment cfg
  end

  cmd 'show configuration' do |cfg|
    cfg.gsub! /^# Exported by \S+ on .*/, '# '
    cfg
  end

  cfg :ssh do
    # User shell must be /etc/cli.sh
    post_login 'set config-lock on override'
    pre_logout 'exit'
  end
end
```

### Extending FortiOS Model to support FortiManager and FortiAnalyzer

- Create a file named: /etc/oxidized/model/fortiman.rb with content
```bash
class FortiMAN < Oxidized::Model
  comment '# '

  prompt /^([-\w.~]+(\s[(\w\-.)]+)?~?\s?[#>$]\s?)$/

  expect /^--More--\s$/ do |data, re|
    send ' '
    data.sub re, ''
  end

  cmd :all do |cfg, cmdstring|
    new_cfg = comment "COMMAND: #{cmdstring}\n"
    new_cfg << cfg.each_line.to_a[1..-2].map { |line| line.gsub(/(conf_file_ver=)(.*)/, '\1<stripped>\3') }.join
  end

  cmd :secret do |cfg|
    # ENC indicates an encrypted password, and secret indicates a secret string
    cfg.gsub! /(set .+ ENC) .+/, '\\1 <configuration removed>'
    cfg.gsub! /(set .*secret) .+/, '\\1 <configuration removed>'
    # A number of other statements also contains sensitive strings
    cfg.gsub! /(set (?:passwd|password|key|group-password|auth-password-l1|auth-password-l2|rsso|history0|history1)) .+/, '\\1 <configuration removed>'
    cfg.gsub! /(set md5-key [0-9]+) .+/, '\\1 <configuration removed>'
    cfg.gsub! /(set private-key ).*?-+END (ENCRYPTED|RSA|OPENSSH) PRIVATE KEY-+\n?"$/m, '\\1<configuration removed>'
    cfg.gsub! /(set ca ).*?-+END CERTIFICATE-+"$/m, '\\1<configuration removed>'
    cfg.gsub! /(set csr ).*?-+END CERTIFICATE REQUEST-+"$/m, '\\1<configuration removed>'
    cfg
  end


  post do
    cfg = []

    cfg << cmd('get system status') do |cfg_hw|
      comment cfg_hw
    end

    cfg << cmd('show')
    cfg.join "\n"
  end

  cfg :telnet do
    username /login:/
    password /^Password:/
  end

  cfg :telnet, :ssh do
    pre_logout "exit\n"
  end
end
```

# Reference
- https://github.com/ytti/oxidized
- https://packetpushers.net/install-oxidized-network-configuration-backup/
- https://codingpackets.com/blog/oxidized-getting-started/