FROM debian:buster

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 redis memcached imagemagick build-essential cython3 webp ffmpeg gifsicle exiftool libjpeg-turbo-progs libcairo2 curl coreutils libexiv2-dev libboost-python-dev python3-setuptools
ADD pip /root/pip/
WORKDIR /root/pip
RUN python3 setup.py install
ADD wheelfiles /root/wheelfiles/
WORKDIR /root/wheelfiles
RUN pip3 install *.whl
WORKDIR /root
ADD thumbor /root/thumbor/
WORKDIR /root/thumbor
RUN make PYTHON=python3 setup test