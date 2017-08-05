export imageName = `docker image list | grep home-switch | awk -F ' ' '{print $3}'`
docker image save $imageName -o ./images/docker-home-switch
