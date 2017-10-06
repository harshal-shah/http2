#!/bin/bash
if [[ "$1" == "rm" ]]; then 
   docker stop $(docker ps -qa);
   docker rm $(docker ps -qa);
fi

docker run -d -p 8080:8080 --name http2server harshals/http2-server:1.3

