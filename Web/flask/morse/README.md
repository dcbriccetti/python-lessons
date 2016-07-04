# Morse Code Secret Server

This project provides Python client and server programs for “unlocking” a server 
via Morse Code and then requesting a secret. It uses the Flask framework 
and the requests library.

## YouTube Video: Demo and Code Walkthrough

[This video](https://www.youtube.com/watch?v=MJ2AF7hZUQE&list=PL7DF0D1EA1E0010FC)
demonstrates the programs and walks through the code.

## The Server

For each IP address connecting to it, the server keeps track of a client’s 
progress in supplying the password in Morse Code, in the right order, 
without timing out. When the password is supplied correctly, access to the 
secret is unlocked for a period of time.

## The Client

A human could use the browser to supply the codes one by one, but that would
be tedious, so we have a client program. For each letter in the password,
the client looks up the Morse Code, and for each element of the Morse Code for
the letter, replaces it with “dash” or “dot” and issues an HTTP GET request
to the server in the form: `/codes/<element>`, where `<element>` is `dash` or `dot`.

Once the client unlocks the secret, it can request the secret with `/secret`.

## The codes Module

The codes model stores the morse code, the password, and dictionaries used to 
substitute “dash” for “-” (yes, this is really a hyphen and not a dash), 
“dot” for “.”, and vice versa. Web browsers may discard a “.” in a URI path,
so we replace the symbols with words.

## Features of Python Used

The server and client use many features of Python, including:

- for ... in
- logging
- generator
- dictionary
- dictionary comprehension
- requests
- Flask
- class
