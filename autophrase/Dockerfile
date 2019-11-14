FROM ubuntu:16.04

ENV WORK_PATH=/autophrase

RUN echo "===> install Java"  && \
    apt-get install -y git maven openjdk-8-jdk && \
    update-java-alternatives --set java-1.8.0-openjdk-amd64

RUN \
    echo "===> install g++" && \
    apt-get update && apt-get install -y --force-yes g++

RUN \
    echo "===> install make, curl, perl" && \
    apt-get update && apt-get install -y --force-yes wget zip make curl perl

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
