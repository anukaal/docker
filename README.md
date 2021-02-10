# Docker Basic commands 

```
Run - start a container 

$ docker run nginx
```
```
ps - list containers

$ docker ps 
$ docker ps -a
```
```
Stop - stop a container

$ docker stop image_name
```
```
Rm - remove a containers

$ docker rm container
```
```
Images - list images

$ docker images
```
```
rmi - Remove Images 

$ docker rmi images
```
```
Pull - Download an image

$ docker pull nginx
```

```
Append a command 

$ docker run ubuntu sleep 5
```
```
Exec - Execute a command

$ docker exec distracted_mcclintock cat /etc/hosts 
```
```
Run - attach and detach

$ docker run –d kodekloud/simple-webapp
```

```
Run - tag

$ docker run redis
$ docker run redis:4.0
```
```
Run - STDIN

$ docker run –it kodekloud/simple-prompt-docker
```

```
Run - PORT mapping

$ docker run –p 80:5000 kodekloud/simple-webapp
$ docker run -p 8306:3306 mysql
```

```
Run - Volume mapping

$  docker run –v /opt/datadir:/var/lib/mysql mysql
```

```
Inspect container

$ docker inspect ubuntu
```

```
Container logs

$ docker logs redis
```

```
ENV Variable in docker

$ docker run -e APP_COLOR=blue simple-webapp-color
```

```
Inspect environment variable

$ docker inspect blissful_hopper
```
```
Docker build 

$ docker build .
```
