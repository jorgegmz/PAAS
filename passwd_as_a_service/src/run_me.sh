#!/usr/bin/env bash

echo "Stopping container"
sudo docker stop cloud-api-service
echo "Remove container"
sudo docker rm cloud-api-service
echo "Build container"
sudo docker build -f ../../Dockerfile --tag cloud-service .
echo "Running container"
sudo docker run -d -v /etc/:/etc/ -p 5000:5000 --name cloud-api-service cloud-service
