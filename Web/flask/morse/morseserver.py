import logging
from time import time
from flask import Flask, request
from codes import morse_code_strings

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('morseserver')
app = Flask(__name__)

PLAIN_HEADER = {'Content-Type': 'text/plain; charset=utf-8'}
PASSPHRASE = 'open sesame'.replace(' ', '')  # Ignore spaces for now
TIMEOUT_SECONDS = 2
SECRET_PATTERN = ''.join((morse_code_strings[letter] for letter in PASSPHRASE))
states_by_addr = {}


class UserState:
    'Stores data needed for each remote user making requests'
    def __init__(self):
        self.elements_matched = 0
        self.last_request_time = time()
        self.locked = True


@app.route('/code/<code>')
def code(code):
    addr = request.remote_addr
    state = states_by_addr.get(addr, UserState())
    states_by_addr[addr] = state
    if time() > state.last_request_time + TIMEOUT_SECONDS:
        log.info('Timed out')
        state.elements_matched = 0
    state.last_request_time = time()
    next_code = SECRET_PATTERN[state.elements_matched]
    if code == next_code:
        state.elements_matched += 1
        if state.elements_matched == len(SECRET_PATTERN):
            state.elements_matched = 0  # Reset so they can run again
            state.locked = False
            log.info(addr + ' unlocked')
            return 'Unlocked!\n', 200, PLAIN_HEADER
        else:
            log.debug('%s elements matched: %d', addr, state.elements_matched)
            return "Keep going.\n", 200, PLAIN_HEADER
    else:
        state.locked = True
        state.elements_matched = 0
        return 'Wrong. Start again.\n', 400, PLAIN_HEADER


@app.route('/secret')
def secret():
    state = states_by_addr.get(request.remote_addr)
    if state and not state.locked:
        return 'The secret is 42\n'

    return 'Give us the passphase via Morse Code first.\n', 403, PLAIN_HEADER


app.run(host='localhost', debug=True, threaded=True)
