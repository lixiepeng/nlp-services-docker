FROM python:3.6.5
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

RUN apt-get update && apt-get install -y -f --no-install-recommends --fix-missing \
    graphviz \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ADD . /work
WORKDIR /work

RUN pip install -r requirements.txt