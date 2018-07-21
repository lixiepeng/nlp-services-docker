FROM python:3.6.5
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

ADD . /work
WORKDIR /work

RUN pip install -r requirements.txt

RUN curl --silent -o total_word_feature_extractor.dat.tar.gz \
 https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz \
    && tar -xzf total_word_feature_extractor.dat.tar.gz && rm -f total_word_feature_extractor.dat.tar.gz