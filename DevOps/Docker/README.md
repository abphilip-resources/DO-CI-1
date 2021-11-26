# Docker Commands

### Image 
    docker image ls                                 --> list all running images
    docker image ls -a                              --> list all images    
    docker build -t <new_image_name> <path>         --> build image from dockerfile
    docker image rm <image_name>                    --> remove image
    docker save -o <file_name> <image_name>         --> save image output to file
    docker load -i <file_name>                      --> load image from file as input

### Container 
    docker container ls                             --> list all running containers
    docker container ls -a                          --> list all containers
    docker container run -it <image_name>           --> run container from image
    >  run -v "%cd%":/<dir> <image_name> bash       --> run container with data volume
    >  run -p 8888:8888 <image_name>                --> run container with port
    docker container exec -it <container_id>        --> run container with shell
    docker container start <container_id>           --> start container
    docker container stop <container_id>            --> stop container
    docker container kill <container_id>            --> stop container immediately
    docker container rm <container_id>              --> remove container
    docker commit <container_name> <image_name>     --> save container as new image

### Compose
    docker-compose build                            --> build all images
    docker-compose up                               --> start all containers
    docker-compose up -d <container_name>           --> start particular container first
    docker-compose down                             --> stop all containers

### Dockerhub
    docker login                                    --> login to dockerhub
    docker tag <image_id> <user>/<repo>:<v>         --> tag image, default version: "latest"
    docker push <user>/<repo>:<v>                   --> push image to dockerhub
    docker pull <user>/<repo>:<v>                   --> pull image from dockerhub