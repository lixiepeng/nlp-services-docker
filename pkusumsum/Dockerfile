from jermainedavis/java-python
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

# github
RUN git clone https://github.com/phiedulxp/PKUSUMSUM-docker.git && \  
cd PKUSUMSUM-docker && \
pip3 install -r requirements.txt && \
cp ./lib/liblpsolve55.so /usr/local/lib/liblpsolve55.so && \
cp ./lib/liblpsolve55j.so /usr/local/lib/liblpsolve55j.so && \
/sbin/ldconfig

WORKDIR /PKUSUMSUM-docker

# dash app
CMD ['python3','server-dash.py']