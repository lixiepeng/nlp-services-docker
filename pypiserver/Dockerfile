FROM continuumio/anaconda

ADD . /work
WORKDIR /work

RUN pip install pypiserver &&\
    pip install -r requirements.txt --download /opt/conda/pkgs 
    #pip download --cache-dir /opt/conda/pkgs -r requirements.txt
    #pip install -r requirements.txt --download /opt/conda/pkgs 
    

EXPOSE 8080

CMD [ "pypi-server", "-p","8080", "--disable-fallback","/opt/conda/pkgs" ]

# RUN pip install pypiserver && \
    # pip install pip2pi

# RUN pip2tgz /opt/conda/pkgs -r requirements.txt