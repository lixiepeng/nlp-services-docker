FROM maven

WORKDIR /work

RUN git clone https://github.com/CogComp/talen.git && \
    cd talen && \
    mvn clean

EXPOSE 8009


CMD [ "./scripts/run.sh" ]

