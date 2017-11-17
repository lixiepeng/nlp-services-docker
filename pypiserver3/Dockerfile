FROM continuumio/anaconda3

ADD . /work
WORKDIR /work

RUN pip install pypiserver && \
    pip install pip2pi

RUN pip2pi /opt/conda/pkgs -r requirements.txt

EXPOSE 8080

CMD [ "pypi-server", "-p","8080", "/opt/conda/pkgs" ]