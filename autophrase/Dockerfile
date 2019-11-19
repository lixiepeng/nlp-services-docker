FROM ubuntu:16.04

ENV WORK_PATH=/autophrase

RUN echo "===> install Java"  && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer

RUN \
    echo "===> install g++" && \
    apt-get update && apt-get install -y --force-yes g++

RUN \
    echo "===> install make, curl, perl" && \
    apt-get update && apt-get install -y --force-yes git wget zip make curl perl

RUN wget https://github.com/shangjingbo1226/AutoPhrase/archive/master.zip && \
    unzip master.zip && \
    rm master.zip && \
    mv AutoPhrase-master $WORK_PATH

RUN \
    echo "===> make" &&\
    cd $WORK_PATH && make

RUN \
    echo "===> clean up..."  && \
    apt-get remove --purge -y --force-yes make gcc && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR $WORK_PATH
