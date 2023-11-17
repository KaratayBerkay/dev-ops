

# Docker CMD Cheatsheet

[repo:](github) https://github.com/BretFisher/udemy-docker-mastery 

``` bash
get Docker via #!/bin/sh : https://get.docker.com/
```
``` bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
``` bash
sh get-docker.sh
```
``` bash
docker exec -it <container> bash
```

# Docker CMD lines
check docker version by  
``` bash
docker version
```
check docker info by  
``` bash
docker info
```

Downloaded image 'nginx' from docker hub Sta.
Started a new container from that image.
Opened port 80 on the host IP.
Routes that traffic to the container IP, port 80.
Give container a friendly name of 'webhost'.
``` bash
docker container run --publish 80:80 --detach --name webhost nginx
```

docker container list
``` bash
docker -ls -a
```

container remove by first three char of id
-f for force
``` bash
docker rm -f 11A 76T
```
``` bash
docker top webhost
```

run a container and add environment variable by -e
``` bash
docker container run --publish 80:80 --detach --name webhost --e ENV_VAR=VALUE nginx
```

inspect, monitor, process a running container
list running processes in container
something like ps aux
``` bash
docker inspect webhost; docker top webhost; docker stats webhost
```

-it means live kernel open and enter in container @run
``` bash
docker container -it
```


# Docker Network

- list available networks of virtual network drivers
``` bash
docker network -ls
```

- inspect a network by name or NetworkID
``` bash
docker network inspect bridge 
```

- create a network
``` bash
docker network create --driver
```

connect container to a network other than default bridge
``` bash
docker network connect 01ce8f7b3f2d d780ddc7f7a9
```
``` bash
docker network disconnect 01ce8f7b3f2d d780ddc7f7a9
```

+ check layers of an image

| Layers    | Hierarcy |
|-----------|----------|
| Image     | 1        |
| Container | 2        |
| Services  | 3        |
| Changes   | 3        |
``` bash
docker history nginx
```
to clean up just "dangling" images
``` bash
docker image prune 
```

``` bash
docker logs webhost
```


will clean up everything you're not currently using
``` bash
docker system prune
```


### Dockerfile
A dockerfile is a shell script that contains all the commands a user could call 
on the command line to assemble an image.
``` dockerfile
FROM nginx:latest

ENV AUTHOR=Docker

WORKDIR /usr/share/nginx/html
# change working directory to root of nginx webhost
# instead using RUN cd /usr/share/nginx/html

RUN apt-get update && apt-get install -y fortunes \
    && rm -rf /var/lib/apt/lists/* \
    && echo "fortune | cowsay" >> /usr/local/bin/entrypoint.sh \
    && chmod +x /usr/local/bin/entrypoint.sh \
    && echo "Welcome to Docker Mastery" > /usr/share/nginx/html/index.html \
    && echo "Dockerfile by $AUTHOR" >> /usr/share/nginx/html/index.html

# difference between && and ; is that && will stop if error and only continue
# if earlier command is successful. ; will continue even if error.

RUN echo "This is a second RUN statement"

EXPOSE 80 443

# Comment
CMD ["nginx", "-g", "daemon off;"]

```





