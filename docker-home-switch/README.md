# How to deploy
```
$ build.sh
$ run.sh
$ export.sh

// transfer output image to Synology
$ ssh <Synology>
Synology[~] # docker load < docker-home-switch
Synology[~] # docker images
Synology[~] # docker run <image-id>
```
