from jermainedavis/java-python
MAINTAINER Xiepeng Li <phiedulxp@gmail.com>

# github
WORKDIR /home/work
RUN git clone https://github.com/phiedulxp/PKUSUMSUM-docker.git

RUN cd PKUSUMSUM-docker

# pip 
RUN pip3 install -r requirements.txt

# lib
RUN cp ./lib/liblpsolve55.so /usr/local/lib/liblpsolve55.so
RUN cp ./lib/liblpsolve55j.so /usr/local/lib/liblpsolve55j.so
RUN  /sbin/ldconfig

# dash app
CMD ['python3','server-dash.py']