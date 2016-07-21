import logging
from time import time
from flask import Flask, request

PLAIN_HEADER = {'Content-Type': 'text/plain; charset=utf-8'}
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('chatserver')
app = Flask(__name__)
messages = []


@app.route('/post/<who>/<message>')
def post_message(who, message):
    messages.append((time(), request.remote_addr, who, message))
    print(messages)
    return "Message saved.\n" + str(messages), 200, PLAIN_HEADER

app.run(host='localhost', debug=True, threaded=True)
