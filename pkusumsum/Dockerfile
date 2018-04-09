FROM python
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

# github
WORKDIR /home/work
RUN git clone https://github.com/phiedulxp/PKUSUMSUM-docker.git && \
cd /home/work/PKUSUMSUM-docker && \
pip install -r requirements.txt && \
add-apt-repository ppa:webupd8team/java -y && \
apt-get update && \
apt-get install oracle-java8-installer
cp ./lib/liblpsolve55.so /usr/local/lib/liblpsolve55.so && \
cp ./lib/liblpsolve55j.so /usr/local/lib/liblpsolve55j.so && \
/sbin/ldconfig

# dash app
CMD ['python','server-dash.py']