#!/usr/bin/python3

import base64
import binascii

def decode_secret(secret):
    secret = secret.replace(' ', '')
    secret = secret.upper()
    secret = secret.encode('ascii')
    secret = base64.b32decode(secret)
    return secret

if __name__ == "__main__":
    secret = input('Google key: ')
    secret = decode_secret(secret)
    print(binascii.hexlify(secret).decode('ascii'))
