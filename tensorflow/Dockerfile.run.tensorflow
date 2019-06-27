# Copyright (c) Microsoft Corporation
# All rights reserved.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# tag: pai.run.tensorflow
#
# Before building this image you need to build the base image first:
#
# docker build -f Dockerfile.build.base -t lixiepeng/pai:hadoop2.7.2-cuda10.0-cudnn7-devel-ubuntu16.04.


FROM lixiepeng/pai:hadoop2.7.2-cuda10.0-cudnn7-devel-ubuntu16.04

ENV TENSORFLOW_VERSION=1.13.1

# For how to run TensorFlow on Hadoop,
# please refer to https://www.tensorflow.org/deploy/hadoop
# --no-cache-dir for MemoryError
RUN pip install --no-cache-dir tensorflow-gpu==${TENSORFLOW_VERSION} sentencepiece && \
    pip3 install --no-cache-dir tensorflow-gpu==${TENSORFLOW_VERSION} sentencepiece

# Add symbol link for libcuda.so
RUN ln -s /usr/local/cuda/targets/x86_64-linux/lib/stubs/libcuda.so \
          /usr/local/cuda/targets/x86_64-linux/lib/stubs/libcuda.so.1

WORKDIR /root
