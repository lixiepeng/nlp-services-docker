FROM alpine:3.7
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>
ENV LANG C.UTF-8

# java
RUN { \
    echo '#!/bin/sh'; \
    echo 'set -e'; \
    echo; \
    echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
  } > /usr/local/bin/docker-java-home \
  && chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r0

RUN set -x \
  && apk add --no-cache \
    openjdk8="$JAVA_ALPINE_VERSION" \
  && [ "$JAVA_HOME" = "$(docker-java-home)" ]

# python  
RUN apk add --update \
    git \
    python \
    python-dev \
    py-pip \
    build-base \
  && rm -rf /var/cache/apk/*

# github
WORKDIR /home/work
RUN git clone https://github.com/phiedulxp/PKUSUMSUM-docker.git && \
cd /home/work/PKUSUMSUM-docker && \
pip install -r requirements.txt && \
cp ./lib/liblpsolve55.so /usr/local/lib/liblpsolve55.so && \
cp ./lib/liblpsolve55j.so /usr/local/lib/liblpsolve55j.so && \
/sbin/ldconfig

EXPOSE 8080
# dash app
CMD ['python','server-dash.py']

