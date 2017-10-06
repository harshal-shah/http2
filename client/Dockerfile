FROM ubuntu:16.04
WORKDIR /app/
ADD . /app/
RUN chmod 755 /app/install_curl.sh && /app/install_curl.sh
ENV HTTP2_SERVER http2server
ENV HTTP2_PORT 8080
CMD sleep 10000
