FROM continuumio/anaconda

ADD . /work
WORKDIR /work

RUN pip install pypiserver && \
    pip install -r requirements.txt

EXPOSE 8080

CMD [ "pypi-server", "-p","8080", "/opt/conda/Lib/site-packages" ]

