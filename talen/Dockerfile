FROM maven

WORKDIR /work

RUN git clone https://github.com/CogComp/talen.git && \
    cd talen && \
    mvn clean && \
    echo "lxp talen2lxp" > config/users.txt && \
    mkdir -p logs && \
    mkdir -p dicts

EXPOSE 8009

CMD ["mvn", "spring-boot:run"]

