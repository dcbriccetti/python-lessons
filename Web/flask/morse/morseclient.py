import requests
from time import sleep
from codes import morse_code_strings

URL_BASE = 'http://localhost:5000'
INTER_LETTER_DELAY = 0.2
SPACE_DELAY = INTER_LETTER_DELAY * 3


def run_with_message(message):
    request_secret()
    send_unlock_request(message)
    request_secret()


def request_secret():
    resp = requests.get(URL_BASE + '/secret')
    print(resp.text)


def send_unlock_request(message):
    for letter in message:
        if letter == ' ':
            sleep(SPACE_DELAY)
        else:
            for symbols in morse_code_strings[letter]:
                for symbol in symbols:
                    resp = requests.get(URL_BASE + '/code/' + symbol)
                    print(resp.text)
            sleep(INTER_LETTER_DELAY)

run_with_message('wrong')
sleep(2)
run_with_message('open sesame')
