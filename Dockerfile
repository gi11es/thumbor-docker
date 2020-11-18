FROM debian:buster

RUN apt-get update && apt-get install --no-install-recommends -y python3 redis memcached imagemagick build-essential cython3 webp ffmpeg gifsicle exiftool libjpeg-turbo-progs libcairo2 curl coreutils libexiv2-dev libboost-python-dev python3-setuptools xcftools libvips-tools librsvg2-bin ghostscript djvulibre-bin ca-certificates xvfb nodejs npm xauth pkg-config libcairo2-dev libjpeg-dev libgif-dev && rm -rf /var/lib/apt/lists/*
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
ADD pyvows /root/pyvows/
WORKDIR /root/pyvows
RUN make setup
ADD core /root/core/
WORKDIR /root/core
RUN make PIP=pip3 setup pyvows_run install
ADD 3d2png /root/3d2png/
ADD 3d2png_node_modules /root/3d2png/node_modules/
WORKDIR /root/3d2png
RUN npm install --unsafe-perm -g .
RUN which 3d2png
ADD thumbor-plugins /root/thumbor-plugins/
WORKDIR /root/thumbor-plugins
RUN make setup test