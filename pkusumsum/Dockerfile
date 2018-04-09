#from jermainedavis/java-python
from ubuntu
from java
from python
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

# github
WORKDIR /home/work
RUN git clone https://github.com/phiedulxp/PKUSUMSUM-docker.git && \
pip3 install --upgrade pip && \ 
cd /home/work/PKUSUMSUM-docker && \
pip3 install -r requirements.txt && \
cp ./lib/liblpsolve55.so /usr/local/lib/liblpsolve55.so && \
cp ./lib/liblpsolve55j.so /usr/local/lib/liblpsolve55j.so && \
/sbin/ldconfig

# dash app
CMD ['python3','server-dash.py']