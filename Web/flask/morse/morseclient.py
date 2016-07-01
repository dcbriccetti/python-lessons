import requests
from time import sleep
from codes import morse_code_strings

URL_BASE = 'http://localhost:5000'
INTER_LETTER_DELAY_MS = 0.2
SPACE_DELAY_MS = INTER_LETTER_DELAY_MS * 3


def run_with_message(message):
    def request_secret():
        resp = requests.get(URL_BASE + '/secret')
        print(resp.text)

    request_secret()

    for letter in message:
        if letter == ' ':
            sleep(SPACE_DELAY_MS)
        else:
            for symbols in morse_code_strings[letter]:
                for symbol in symbols:
                    resp = requests.get(URL_BASE + '/code/' + symbol)
                    print(resp.text)
            sleep(INTER_LETTER_DELAY_MS)

    request_secret()

for message in ('wrong', 'open sesame'):
    run_with_message(message)
    sleep(3)
