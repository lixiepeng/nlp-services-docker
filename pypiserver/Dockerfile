FROM continuumio/anaconda

WORKDIR /work

RUN pip install pypiserver && \
    git clone https://github.com/phiedulxp/tweet_search.git
    
WORKDIR /work/tweet_search
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "pypi-server", "-p","8080", "/opt/conda/Lib" ]

