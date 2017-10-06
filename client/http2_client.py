import json
import ssl
from hyper import HTTP20Connection

myssl = ssl.create_default_context();
myssl.check_hostname=False
myssl.verify_mode=ssl.CERT_NONE

conn = HTTP20Connection('localhost', 8080, secure=True, ssl_context=myssl)
conn.request('GET', '/')
resp = conn.get_response()

# process initial page with book ids
index_data = json.loads(resp.read().decode("utf8"))

responses = []
chunk_size = 100

# split initial set of urls into chunks of 100 items
for i in range(0, len(index_data), chunk_size):
    request_ids = []

    # make requests
    for _id in index_data[i:i+chunk_size]:
        book_details_path = "/book?id={}".format(_id)
        request_id = conn.request('GET', book_details_path)
        print("Created request ID {}".format(request_id))
        request_ids.append(request_id)

    # get responses
    for req_id in request_ids:
        print("Sending req ID {} to fetch".format(req_id))
        response = conn.get_response(req_id)
        body = json.loads(response.read().decode("utf8"))
        responses.append(body)

assert len(responses) == 3000