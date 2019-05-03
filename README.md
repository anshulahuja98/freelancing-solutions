# freelancing-solutions  ![Build status](https://travis-ci.com/anshulahuja98/freelancing-solutions.svg?token=sxKTXczsK8R6uvz4sAHy&branch=master) [![Coverage Status](https://coveralls.io/repos/github/anshulahuja98/freelancing-solutions/badge.svg?branch=master)](https://coveralls.io/github/anshulahuja98/freelancing-solutions?branch=master)
A freelancing platform project for course *CS223(Software Engineering)*

### Steps to deploy
1. Install [Docker](https://docs.docker.com/install/)
1. Pull the [docker image of the project from dockerhub](https://cloud.docker.com/repository/docker/anshulahuja/freelancing-solutions) 

    ```
    docker pull anshulahuja/freelancing-solutions
    ```
1. Run a container of the image 
    ```
    docker run -p 80:8000 anshulahuja/freelancing-solutions
    ```
   This will start the server exposed at port 80 of your system

