#TODO this can probably be removed, this doesn't use pytorch
# install right version of CUDA for the version of Pytorch used
# FROM nvidia/cuda:12.0.1-devel-ubuntu18.04

#TODO just install a tensorflow docker container for the version I want of 2.7.0
FROM tensorflow/tensorflow:2.7.0-gpu

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

# CUDA includes
ENV CUDA_PATH /usr/local/cuda
ENV CUDA_INCLUDE_PATH /usr/local/cuda/include
ENV CUDA_LIBRARY_PATH /usr/local/cuda/lib64

# Ubuntu Packages
RUN apt-get update -y && apt-get install software-properties-common -y && \
    add-apt-repository -y multiverse && apt-get update -y && apt-get upgrade -y && \
    apt-get install -y apt-utils nano vim man build-essential wget sudo && \
    rm -rf /var/lib/apt/lists/*

# Install curl and other dependencies
RUN apt-get update -y && apt-get install -y curl libssl-dev openssl libopenblas-dev \
    libhdf5-dev hdf5-helpers hdf5-tools libhdf5-serial-dev libprotobuf-dev protobuf-compiler git

# Install python3 pip
RUN apt-get update
RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip

# Python packages we use
RUN pip3 install matplotlib==3.3.4
RUN pip3 install numpy==1.19.5
RUN pip3 install scikit-learn==0.24.2
RUN pip3 install scikit-optimize==0.9.0
RUN pip3 install scipy==1.5.4
RUN pip3 install deepxde==1.8.0
RUN pip3 install jupyterlab
RUN pip3 install numba

WORKDIR /cee598
