[![YourActionName Actions Status](https://github.com/gi11es/thumbor-docker/workflows/Wikimedia%20Thumbor%20Python%20plugins%20linting/badge.svg)](https://github.com/gi11es/thumbor-docker/actions)
[![YourActionName Actions Status](https://github.com/gi11es/thumbor-docker/workflows/Dockerfile%20linting/badge.svg)](https://github.com/gi11es/thumbor-docker/actions)
[![YourActionName Actions Status](https://github.com/gi11es/thumbor-docker/workflows/Docker%20build/badge.svg)](https://github.com/gi11es/thumbor-docker/actions)

Docker environment to run Thumbor and the Wikimedia Thumbor plugins on Debian Buster/Python 3.

Once the docker image is running using a command like the one in run.sh, you can try it out with this test request:

http://localhost:8800/thumbor/unsafe/300x/gilles.jpg

The files that the running Thumbor instance can work with are in the "files" folder.