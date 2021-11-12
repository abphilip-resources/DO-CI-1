# Docker Commands

### Image 
    docker image ls                             --> list all running images
    docker image ls -a                          --> list all images    
    docker build -t <new_image_name> .          --> build image from dockerfile
    docker image rm <image_name>                --> remove image

### Container 
    docker container ls                         --> list all running containers
    docker container ls -a                      --> list all containers
    docker container run -it <image_name>       --> run container from image
    > -v "%cd%":/data <image_name> bash         --> run container with data volume
    > -p 8888:8888 <image_name>                 --> run container with port
    docker container stop <container_id>        --> stop container
    docker container rm <container_id>          --> remove container

### Dockerhub
    docker login                                --> login to dockerhub
    docker tag <image_id> <user>/<repo>:<v>     --> tag image, default version: "latest"
    docker push <user>/<repo>:<v>               --> push image to dockerhub
    docker pull <user>/<repo>:<v>               --> pull image from dockerhub