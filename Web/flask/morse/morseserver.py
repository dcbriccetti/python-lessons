import logging
from time import time
from flask import Flask, request, abort
from codes import morse_code_strings

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('morseserver')
app = Flask(__name__)

PLAIN_HEADER = {'Content-Type': 'text/plain; charset=utf-8'}
PASSPHRASE = 'open sesame'.replace(' ', '')  # Ignore spaces for now
TIMEOUT_SECONDS = 2
SECRET_PATTERN = ''.join((morse_code_strings[letter] for letter in PASSPHRASE))
states_by_remote_addr = {}


class UserState:
    def __init__(self, elements_matched, last_request_time):
        self.elements_matched = elements_matched
        self.last_request_time = last_request_time
        self.locked = True


@app.route('/code/<code>')
def code(code):
    addr = request.remote_addr
    state = states_by_remote_addr.get(addr, UserState(0, 0))
    states_by_remote_addr[addr] = state
    if state.last_request_time != 0 and time() > state.last_request_time + TIMEOUT_SECONDS:
        log.info('Timed out')
        state.elements_matched = 0
    state.last_request_time = time()
    next_char = SECRET_PATTERN[state.elements_matched]
    if code == next_char:
        if state.elements_matched == len(SECRET_PATTERN) - 1:
            state.elements_matched = 0
            state.locked = False
            log.info(addr + ' unlocked')
            return 'Unlocked!', 200, PLAIN_HEADER
        else:
            state.elements_matched += 1
            log.debug('%s elements matched: %d', addr, state.elements_matched)
            return "Keep going.", 200, PLAIN_HEADER
    else:
        state.locked = True
        state.elements_matched = 0
        return 'Wrong. Start again.', 400, PLAIN_HEADER


@app.route('/secret')
def secret():
    state = states_by_remote_addr.get(request.remote_addr)
    if state and not state.locked:
        return 'The secret is 42\n'

    return 'Give us the passphase via Morse Code first.', 403, PLAIN_HEADER


app.run(host='0.0.0.0', debug=True, threaded=True)
