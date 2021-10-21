## Installation

- Ubuntu: apt-get install nginx
- CentOS: yum install nginx
- Docker: docker pull nginx

## Configuration

### Two server block, serving static files
```nginx
http {
  index index.html;

  server {
    server_name www.domain1.com;
    access_log logs/domain1.access.log main;

    root /var/www/domain1.com/htdocs;
  }

  server {
    server_name www.domain2.com;
    access_log  logs/domain2.access.log main;

    root /var/www/domain2.com/htdocs;
  }
}
```

### Default Catch All Server Block
```nginx
http {
  index index.html;

  server {
    listen 80 default_server;
    server_name _; # This is just an invalid value which will never trigger on a real hostname.
    access_log logs/default.access.log main;

    server_name_in_redirect off;

    root  /var/www/default/htdocs;
  }
}
```

### Wildcard subdomain
```nginx
server_name star.yourdomain.com *.yourdomain.com; # Alternately: _
```

### Reverse Proxy with Caching
```nginx
http {
    proxy_cache_path  /data/nginx/cache  levels=1:2    keys_zone=STATIC:10m
    inactive=24h  max_size=1g;
    server {
        location / {
            proxy_pass             http://1.2.3.4;
            proxy_set_header       Host $host;
            proxy_buffering        on;
            proxy_cache            STATIC;
            proxy_cache_valid      200  1d;
            proxy_cache_use_stale  error timeout invalid_header updating
                                   http_500 http_502 http_503 http_504;
        }
    }
}
```

### SSL Certificate
```nginx
http {
    ssl_password_file /etc/keys/global.pass;
    server {
    	listen 80;
	listen 443  ssl;
	server_name	server.domain.com;
	ssl_certificate /etc/nginx/conf.d/domain.cer;	
        ssl_certificate_key /etc/nginx/conf.d/domain.key;
	location / {
        	......
        	}
		access_log /etc/nginx/conf.d/backupaccess.log main;
	}
}
```

### Prevent accessing default page using ip
```nginx
server {
   	listen	80 default_server;
    	server_name "";
    	return      444;
	}
```

### Return inline html
```nginx
server {
   	listen	80 default_server;
    	server_name "";
    	location / {
		add_header Content-Type text/html;
		return 200 '<html><body>$remote_addr</body></html>';
}
```

### Block to root, but allow to specific file
```nginx
server {
        listen 80;
        server_name 10.10.10.10;
        root /storage/block;
        location / { return 444; }
        #location = / { }
        location = /block.png {}
}
```

## Some Errors

### Docker: Cannot load certificate when specifiying certificate in same folder: ssl_certificate cert.crt
- In fact host volume is /etc/nginx mapping to /etc/nginx/conf.d
```nginx
error_log /etc/nginx/conf.d/error.log debug;
management    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
management    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
management    | /docker-entrypoint.sh: Configuration complete; ready for start up
management    | 2021/07/12 15:48:40 [emerg] 1#1: cannot load certificate "/etc/nginx/cert.crt": BIO_new_file() failed (SSL: error:02001002:system library:fopen:No such file or directory:fopen('/etc/nginx/cewa.crt','r') error:2006D080:BIO routines:BIO_new_file:no such file)
management    | nginx: [emerg] cannot load certificate "/etc/nginx/cert.crt": BIO_new_file() failed (SSL: error:02001002:system library:fopen:No such file or directory:fopen('/etc/nginx/cewa.crt','r') error:2006D080:BIO routines:BIO_new_file:no such file)
```

- Solution: use ssl_certificate /etc/nginx/conf.d/cert.crt

### “http” directive is not allowed here in <config file>
- Reason: there are http in parent configuration and this configuration is included in that one
- Solution: remove http {} section from mentioned configuration file

# Reference

- https://www.freecodecamp.org/news/the-nginx-handbook/
- https://www.nginx.com/resources/wiki/start/
- NGINX with LDAP Authentication: https://www.nginx.com/blog/nginx-plus-authenticate-users/
- HTTP Load Balancer: https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/
- https://my.godaddy.com/help/nginx-on-centos-7-install-a-certificate-27192
- https://www.nginx.com/blog/secure-distribution-ssl-private-keys-nginx/
- NGINX Tutorial: https://www.javatpoint.com/nginx-tutorial