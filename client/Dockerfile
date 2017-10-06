FROM ubuntu:16.04
WORKDIR /app/
ADD . /app/
RUN chmod 755 /app/install_curl.sh && /app/install_curl.sh
ENV HTTP2_SERVER http2server
ENV HTTP2_PORT 8080
ENV HTTP2_GET_COUNT 10
ENV HTTP2_POST_COUNT 10
CMD python3 http2_client.py
