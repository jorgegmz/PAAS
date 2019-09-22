#!/usr/bin/bash

echo "Stopping container"
sudo docker stop passwd-as-a-service
echo "Removing container"
sudo docker rm passwd-as-a-service
echo "Building container"
sudo docker build -f Dockerfile --tag passwd-service .
echo "Running container"
sudo docker run -d -v /etc/:/etc/ -p 5000:5000 --name passwd-as-a-service passwd-service
