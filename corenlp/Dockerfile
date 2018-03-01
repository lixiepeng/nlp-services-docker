FROM java:8

ENV CORENLP_ARCHIVE_VERSION=2018-02-27
ENV CORENLP_ARCHIVE=stanford-corenlp-full-${CORENLP_ARCHIVE_VERSION}.zip \
  CORENLP_PATH=/corenlp

RUN wget http://nlp.stanford.edu/software/$CORENLP_ARCHIVE \
  && unzip $CORENLP_ARCHIVE \
  && mv $(basename ../$CORENLP_ARCHIVE .zip) $CORENLP_PATH \
  && rm $CORENLP_ARCHIVE

WORKDIR $CORENLP_PATH

EXPOSE 9000
CMD ["java", "-mx4g", "-cp", "*", "edu.stanford.nlp.pipeline.StanfordCoreNLPServer", "9000"]