##
# phantomjs python Flask selenium and littlewey/home-switch
##
FROM python:2.7.13-jessie
MAINTAINER littlewey, forked from https://github.com/littlewey/home-switch/tree/master/docker-home-switch
USER root
RUN apt-get update -y && apt-get install -y  \
       python-pip \
       fontconfig \
       wget \
    && pip install -U pip \
    && pip install Flask==0.10.1 selenium==3.4.3 bs4==0.0.1 \
    && mkdir -p /app \
    && mkdir -p /usr/share \
    && cd /usr/share \
    && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  \
    && tar xjf phantomjs*.tar.bz2 \
    && ln -s /usr/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs \
    && rm phantom*.bz2 \
    && phantomjs --version \
    && echo "root:root" | chpasswd \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf ~/.cache/pip 
EXPOSE 5000
ADD docker-resource/app.py /app
ADD docker-resource/config.py /app
ADD docker-resource/switch.py /app
ADD docker-resource/credential.py /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]

