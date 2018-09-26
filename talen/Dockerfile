FROM maven

WORKDIR /work

RUN git clone https://github.com/CogComp/talen.git && \
    cd talen && \
    maven mvn clean

EXPOSE 8009


CMD [ "./scripts/run.sh" ]

