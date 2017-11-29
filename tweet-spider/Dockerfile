FROM python:2.7.12

ADD ./ /work
WORKDIR /work
RUN pip install -r requirements.txt

RUN git clone https://github.com/phiedulxp/tweet_search.git
WORKDIR /work/tweet_search


CMD ["git", "pull", "&&", "python", "./spider/worker.py"]
