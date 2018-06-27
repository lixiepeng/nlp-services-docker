FROM ubuntu:16.04

RUN mkdir -p /usr/local/proxy-server \
COPY proxy-server-20171116/ /usr/local/proxy-server

RUN apt-get update && apt-get install -y --no-install-recommends --fix-missing \
    openjdk-9-jdk-headless \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
    && cd /usr/local/proxy-server/bin \
    && chmod +x startup.sh

WORKDIR /usr/local/proxy-server/bin

EXPOSE 8090
EXPOSE 4900
EXPOSE 4993
EXPOSE 50000-50999

CMD ["bash", "startup.sh"]

