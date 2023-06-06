#!/bin/bash

docker0="ubuntu0"
# download the image
docker pull ubuntu

# create volume in /var/lib/docker/volumes/
docker volume create $docker0"_volume"

# run the image
docker run -m 2048m --cpus 0.5 -dti --name $docker0 -v $docker0"_volume":/$docker0"_volume" ubuntu

# show info
docker ps
docker inspect $docker0

# enter container
docker exec $docker0 apt-get update
docker exec $docker0 apt-get upgrade -y
docker exec -it $docker0 /bin/bash
