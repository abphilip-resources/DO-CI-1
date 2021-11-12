# Docker Commands

### Image 
    docker image ls                         --> list all running images
    docker image ls -a                      --> list all images    
    docker build -t <new_image_name> .      --> build image
    docker image rm <image_name>            --> remove image

### Container 
    docker container ls                     --> list all running containers
    docker container ls -a                  --> list all containers
    docker container run -it <image_name>   --> run image
    docker container stop <container_id>    --> stop container
    docker container rm <container_id>      --> remove container

### Dockerhub
    docker login                             --> login to dockerhub
    docker push <image_name>                 --> push image to dockerhub
    docker pull <image_name>                 --> pull image from dockerhub