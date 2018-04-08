FROM ubuntu:16.04
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends --fix-missing \
    ca-certificates \
    curl \
    git \
    unzip \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# python
RUN apt-get install software-properties-common && \
    add-apt-repository ppa:jonathonf/python-3.6

RUN apt-get update \
 && apt-get install -y curl unzip \
    python3.6 python3-setuptools \
 && ln -s /usr/local/bin/python3.6 /usr/bin/python \
 && easy_install3 pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# JAVA
ARG JAVA_MAJOR_VERSION=8
ARG JAVA_UPDATE_VERSION=131
ARG JAVA_BUILD_NUMBER=11
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}

ENV PATH $PATH:$JAVA_HOME/bin
RUN curl -sL --retry 3 --insecure \
  --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
  "http://download.oracle.com/otn-pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/d54c1d3a095b4ff2b6607d096fa80163/server-jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \
  | gunzip \
  | tar x -C /usr/ \
  && ln -s $JAVA_HOME /usr/java \
  && rm -rf $JAVA_HOME/man

# github
WORKDIR /home/work
RUN git clone https://github.com/phiedulxp/PKUSUMSUM-docker.git
RUN cd PKUSUMSUM

# pip 
RUN pip install -r requirements.txt

# lib
RUN cp ./lib/liblpsolve55.so /usr/local/lib/liblpsolve55.so
RUN cp ./lib/liblpsolve55j.so /usr/local/lib/liblpsolve55j.so
RUN  /sbin/ldconfig

# dash app
CMD ['python','server-dash.py']