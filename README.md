# flask-mongo-dockerized
Get start project created on Python Flask and mongodb database. Dockerized with Dockerfile and docker-compose.yaml files

# About
A docker container running Flask app connected with mongoDB. 

# HOW TO RUN
To create the docker container, follow the steps below
1. docker-compose build
2. docker-compose up

Flask service will be open at port 5000, VISIT http://localhost:5000 to test the working.

API - http://localhost:5000/find => to see data presented in Database.
API - http://localhost:5000/insert => to add a new entry in mongo Database.
