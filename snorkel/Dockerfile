FROM continuumio/anaconda

RUN git clone https://github.com/phiedulxp/snorkel.git && \
    cd snorkel && \
    conda install numba && \
    pip install --requirement python-package-requirement.txt && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

EXPOSE 8888

ENTRYPOINT ["tini", "--"]

CMD [ "/bin/bash" ,"./run.sh"]

