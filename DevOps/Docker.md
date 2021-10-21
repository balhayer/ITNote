# Installation

## Ubuntu

- sudo apt-get install docker.io: install docker
- sudo apt-get install docker-compose: install docker compose

# Manage Docker as a non-root user

- Create docker group: sudo groupadd docker
- Add user to docker group: sudo usermod -aG docker $USER
- Logout and Login for the changes to take effect, on Linux can use command instead: newgrp docker
- Test if user can run docker without sudo: docker run hello-world

# Enable Docker service to start automatically

- Sudo systemctl enable docker.service

# DockerFile

- Program to create an image
- Run with docker build: docker build -t <name of result> . (dot is current directory)
- Caching with each step:
    - This is important, watch the build output for “using cache”
    - Docker skips lines that have not changed since the last build
    - The parts that change the most belong at the end of the dockerfile
- Dockerfiles look like shell script, but are not shell scripts
- Processes started on one line will not be running on the next line
    - If you use ENV command, remember that each line is its own call to docker run
- FROM statement:
    - Which image to download and start from
    - Must be the first command in dockerfile
- MAINTAINER statement:
    - Defines the author of this dockerfile
    - Example: MAINTAINER Firstname lastName <email>
- RUN Statement:
    - Run the command, waits for it to finish, and saves the result
    - Example:
        - RUN unzip install.zip /opt/install
        - RUN echo hello world
- ADD Statement
    - Add local files
    - Examples: ADD <file on host> <file in container>
        - ADD run.sh /run.sh
        - Add the content of tar archives: ADD project.tar.gz /install/ (uncompress and add content)
    - Add from URL: ADD http://site.com/path/file.rpm /project/
- ENV Statement
    - Set environmental variables
    - Both during the build and when running the result
    - Example: ENV DB_HOST=db.production.example.com
- ENTRYPOINT and CMD Statements:
    - ENTRYPOINT specifies the start of the command to run
    - CMD specifies the whole command to run
- If you have both, they are combined together
- If your container acts like a command-line program, you can use ENTRYPOINT
- Shell form vs exec form: both can use both
    - Shell form: nano note.txt
    - Exec form: [“/bin/nano”,”note.txt”]
- EXPOSE statement
    - Maps a port into a container
        - EXPOSE 8080
- VOLUME Statement
    - Defines shared or ephemeral volume
    - Example:
        - VOLUME [“host/path” “container/path”]
        - VOLUME [“/shared-data”]
- WORKDIR statement
    - Sets the directory the container starts in
    - Example: WORKDIR /install/
- USER Statement
    - Sets which user the container will run as
    - Example:
        - USER User1
        - USER 1000

## Example
```dockerfile
#Dockerfile to build uwsgi-nginx-flask docker
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
```

```dockerfile
#Dockerfile to build ubuntu with python and gunicorn
FROM ubuntu:latest
RUN apt update && apt -y install python3 python3-pip gunicorn
RUN pip install flask
```

# Docker Commands

## Docker run: Run a docker container

### Options

- –name: name container instead of using random name
- -v: volume: map <host directory>:<container directory>:<mode>
- -d: run in daemon mode
- -p: expose <host>:<container> port
- –restart: automatically restart container
    - no: default
    - on-failure: Restart the container if it exits due to an error, which manifests as a non-zero exit code.
    - always: Always restart the container if it stops. If it is manually stopped, it is restarted only when Docker daemon restarts or the container itself is manually restarted
    - unless-stopped: Similar to always, except that when the container is stopped (manually or otherwise), it is not restarted even after Docker daemon restarts.

### Example

- docker run –name webserver -v /storage/www:/usr/share/nginx/html:ro -d -p 80:80 nginx: run nginx container

## Docker update: change setting of container

### Example:

- docker update –restart unless-stopped webserver: change restart policy for container webserver
- docker update –restart unless-stopped $(docker ps -q): change restart policy for all running containers

## Docker ps: list containers

### Example:

- docker ps -a: list all container
- docker ps: list running container
- docker ps -q: list running container in quiet mode (list only ID)
- docker ps -s: display file size
- docker ps -l: show latest created container
- docker ps -n <number>: list latest number created container

## Docker inspect: view all settings of container in json format

### Example:

- docker inspect <docker name>
- docker inspect threatfeed | jq .[0].HostConfig.Binds

# Docker Compose

- A tool to run multiple containers
- Insllation: apt install docker-compose

## Commands:
- docker-compose up [-d]
- docker-compose down
- docker-compose restart <container name>

## Example of docker-compose.yml 
- Running 1 nginx proxy named management, 1 oxidized and 1 backupmgmt
```dockerfile
version: '3'

services:
    management:
        image: nginx
        container_name: management
        ports:
            - 10.10.10.1:80:80
            - 10.10.10.1:443:443
        volumes:
            - /etc/nginx:/etc/nginx/conf.d/
            - /storage:/storage
            - /etc/localtime:/etc/localtime:ro
        restart: always
        extra_hosts:
        - "host.docker.internal:host-gateway"

    oxidized:
        depends_on:
            - management
        image: oxidized:latest
        container_name: oxidized
        expose:
            - "8888"
        volumes:
            - /etc/oxidized:/root/.config/oxidized
            - /etc/localtime:/etc/localtime:ro
        restart: always
        command: /root/.config/oxidized/startup.sh

    backupmgmt:
        depends_on:
            - management
        image: gunicorn
        container_name: backupmgmt
        expose:
            - "80"
        volumes:
            - /storage/backupmanagement:/app
            - /storage/backup:/storage/backup
        command: /app/gunicorn.sh
```

# Some Errors

## nginx: [emerg] host not found in upstream “host.docker.internal:8888” in /etc/nginx/conf.d/nginx.conf:3
- nginx container is configured as a proxy for a another container named oxidizedcontainer

### Configuration of NGINX:
```nginx
upstream oxidizedcontainer{
	server host.docker.internal:8888;
}

server {
	listen 443  ssl;
	server_name	host.domain.com;
	ssl_certificate /etc/nginx/conf.d/bundle.crt;
	ssl_certificate_key /etc/nginx/conf.d/private.key;
	location / {
        	proxy_pass http://oxidizedcontainer/;
		auth_basic "Oxidized";
		auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
		proxy_set_header Host $http_host;
        	}
		access_log /etc/nginx/conf.d/access.log main;
	}
```

- **Reason**: docker can’t find host defined in upstream

### Solution 1: Using extra_hosts: host.docker.internal

- Nginx uses host IP to access upstream. This requires -p <host port>:<container port> on upstream containers
- External users can access upstream container directly if -p listen on 0.0.0.0 or external IP

```dockerfile
version: '3'

services:
    management:
        image: nginx
        container_name: management
        ports:
            - 10.10.10.1:80:80
            - 10.10.10.1:443:443
        volumes:
            - /etc/nginx:/etc/nginx/conf.d/
            - /storage:/storage
            - /etc/localtime:/etc/localtime:ro
        restart: always
        extra_hosts:
        - "host.docker.internal:host-gateway"
```

### Solution 2

- Using docker-compose to run both proxy and oxidizedcontainer
- Using this, oxidized container doesn’t need to be published, just need to be exposed. This is because by default Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name.

#### Configuration of docker-compose.yml
```dockerfile
version: '3'

services:
    proxy:
        image: tiangolo/uwsgi-nginx-flask:latest
        container_name: management
        ports:
            - 10.10.10.1:80:80
            - 10.10.10.1:443:443
        volumes:
            - /etc/nginx:/etc/nginx/conf.d/
            - /etc/www:/app
            - /storage:/storage
        restart: always

    oxidized:
        depends_on:
            - management
        image: oxidized:latest
        container_name: oxidized
        expose:
            - "8888"
        volumes:
            - /etc/oxidized:/root/.config/oxidized
            - /etc/localtime:/etc/localtime:ro
        restart: always
```

#### Configuration of nginx.conf
```nginx
upstream oxidizedcontainer{
	server oxidized:8888;
}

server {
	listen 80;
	server_name	host.domain.com;
	location / {
        	proxy_pass http://oxidizedcontainer;
		auth_basic "Oxidized";
		auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
        	}
		access_log /etc/nginx/conf.d/access.log main;
	}
```

# Some Scenarios

## Creating an docker image to host python app with gunicorn

### Manual Installation
```bash
Run ubuntu docker image: docker run -it -name ubuntu ubuntu
Update docker OS: apt-get update
Install python3: apt-get install python3
Install pip: apt-get install python3-pip
Install gunicorn: apt-get install gunicorn
```

### Automatic Installation using Dockerfile
```dockerfile
FROM ubuntu:latest
RUN apt update && apt -y install python3 python3-pip nginx gunicorn
RUN pip install flask
```
# Reference

- https://stackoverflow.com/questions/38346847/nginx-docker-container-502-bad-gateway-response
- https://stackoverflow.com/questions/45717835/docker-proxy-pass-to-another-container-nginx-host-not-found-in-upstream
- https://dev.to/natterstefan/docker-tip-how-to-get-host-s-ip-address-inside-a-docker-container-5anh
- https://megamorf.gitlab.io/2020/09/19/access-native-services-on-docker-host-via-host-docker-internal/