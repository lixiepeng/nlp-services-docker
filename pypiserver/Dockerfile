FROM continuumio/anaconda

RUN pip install pypiserver

EXPOSE 8080

CMD [ "pypi-server", "-p","8080", "/opt/conda/Libs" ]