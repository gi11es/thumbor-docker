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
# Test build stops here, below is the setup for local development
RUN rm -rf /root/thumbor-plugins/tests
ADD config/tinyrgb.icc /usr/local/lib/thumbor/tinyrgb.icc
RUN mkdir -p /thumbor/tmp
RUN mkdir -p /thumbor/files
ADD config/local /etc/thumbor.d/
RUN dd if=/dev/urandom of=- bs=1024 count=1 2>/dev/null | md5sum -b - | cut -d' ' -f1 > /etc/thumbor.key
ENV TMPDIR=/thumbor/tmp
ENV MAGICK_TEMPORARY_PATH=/thumbor/tmp
ENV MAGICK_DISK_LIMIT=900MB
ENV MAGICK_MEMORY_LIMIT=900MB
EXPOSE 8800
CMD /usr/local/bin/thumbor --port 8800 --keyfile /etc/thumbor.key --conf /etc/thumbor.d/ -l debug