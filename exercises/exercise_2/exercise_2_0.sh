# c) Create a docker image with name ex0-image

docker build --tag ex0-image ./

# Verify and inspect
docker image ls
docker history ex0-image
docker inspect ex0-image


# d) Spin up your docker container and name it ex0-container.

docker container run --name ex0-container ex0-image

# Verify and inspect
docker container ls -a
docker inspect ex0-container
docker logs ex0-container


# e) Go into your container and make sure that these packages are installed.

# Create image and start container, enter bash
docker run --interactive --tty ex0-image /bin/bash

# Enter bash in an already running container
docker exec --interactive --tty ex0-container /bin/bash


# h) Spin up the container in interactive mode. Here are some stuffs you can explore

# count all files and folders inside app/
ls -la /usr/src/app | wc -l

# check your operative system
uname -a
cat /etc/os-release 2>/dev/null || sw_vers

# check the current date
date
TZ=UTC date
