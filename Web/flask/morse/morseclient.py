import requests
from time import sleep
from codes import PASSWORD, morse_codes, words_by_symbol

URL_BASE = 'http://localhost:5000'
INTER_LETTER_DELAY = 0.2


def request_secret():
    response = requests.get(URL_BASE + '/secret')
    print(response.text)


def send_unlock_request(message):
    for letter in message:
        symbols_for_letter = morse_codes[letter]
        for symbol in symbols_for_letter:
            response = requests.get(URL_BASE + '/code/' + words_by_symbol[symbol])
            print(response.text)
        sleep(INTER_LETTER_DELAY)


request_secret()
send_unlock_request(PASSWORD)
request_secret()
