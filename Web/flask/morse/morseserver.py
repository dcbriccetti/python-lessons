import logging
from time import time
from flask import Flask, request
from codes import PASSWORD, morse_codes, symbols_by_word

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('morseserver')
app = Flask(__name__)

PLAIN_HEADER = {'Content-Type': 'text/plain; charset=utf-8'}
STAY_UNLOCKED_SECS = 20
TIMEOUT_SECONDS = 10
SECRET_PATTERN = ''.join((morse_codes[letter] for letter in PASSWORD))
states_by_addr = {}


class UserState:
    'Stores data needed for each remote user making requests'
    def __init__(self):
        self.elements_matched = 0
        self.last_request_time = time()
        self.unlocked_at = None  # The time last unlocked, or None if locked


@app.route('/code/<code_word>')
def code(code_word):
    code = symbols_by_word.get(code_word)
    if not code:
        return 'Must be dash or dot.', 404, PLAIN_HEADER
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
            state.unlocked_at = time()
            log.info(addr + ' unlocked')
            return 'Unlocked!', 200, PLAIN_HEADER
        else:
            log.debug('%s elements matched: %d', addr, state.elements_matched)
            return "Keep going.", 200, PLAIN_HEADER
    else:
        state.unlocked_at = None
        state.elements_matched = 0
        return 'Wrong. Start again.', 400, PLAIN_HEADER


@app.route('/secret')
def secret():
    state = states_by_addr.get(request.remote_addr)
    if state and state.unlocked_at and state.unlocked_at > time() - STAY_UNLOCKED_SECS:
        return 'The secret is 42'

    return ('Give the password via Morse Code, then request the secret within %d seconds.' %
            STAY_UNLOCKED_SECS, 403, PLAIN_HEADER)


app.run(host='localhost', debug=True, threaded=True)
