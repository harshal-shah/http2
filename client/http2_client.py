import json
import subprocess
import ssl
import os
import logging
import sys
import time

HTTP2_SERVER = os.environ['HTTP2_SERVER']
HTTP2_PORT = os.environ['HTTP2_PORT']
HTTP2_GET_COUNT = int(os.environ['HTTP2_GET_COUNT'])
HTTP2_POST_COUNT = int(os.environ['HTTP2_POST_COUNT'])

def _get_base_url():
    return "https://" + HTTP2_SERVER + ':' + HTTP2_PORT + '/'


def _get_books():
    with open('books.json', mode='r') as fh:
        books = json.loads(fh.read())
        return books


def http2_get():
    books = _get_books()
    keylist = list(books.keys())
    for n in range(1, HTTP2_GET_COUNT):
        res = subprocess.run(["curl", "-k", "-X", "GET", "-s", "--http2", _get_base_url() + 'book?id={}'.format(keylist[n])], stdout=subprocess.PIPE)
        logging.info("HTTP2 GET Req # {} : {}".format(n, res.stdout))


def http2_post():
    books = _get_books()
    keylist =list( books.keys())
    for n in range(1, HTTP2_POST_COUNT):
        res = subprocess.run(["curl", "-k", "-X", "POST", "-s", "--http2", "-d", str(books[keylist[n]]), _get_base_url() + 'book'], stdout=subprocess.PIPE)
        logging.info("HTTP2 POST Req # {} : {}".format(n, books[keylist[n]]))


if __name__ == "__main__":
    while True:
        logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, stream=sys.stdout)
        http2_get()
        http2_post()
        time.sleep(30)
