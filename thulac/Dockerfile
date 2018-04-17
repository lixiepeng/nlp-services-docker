FROM python

RUN pip install hug && \
pip install thulac && \
git clone https://github.com/thunlp/THULAC.so.git && \
cd THULAC.so && \
make && \
cp libthulac.so /usr/local/lib/python3.6/site-packages/thulac/libthulac.so

ADD . /THULAC.so
WORKDIR /THULAC.so

EXPOSE 8000
CMD hug -f thulac-service.py