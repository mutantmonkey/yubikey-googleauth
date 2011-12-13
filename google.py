#!/usr/bin/python3
################################################################################
# google.py - google authenticator via yubikey
#
# author: mutantmonkey <mutantmonkey@mutantmonkey.in>
################################################################################

import base64
import binascii
import hashlib
import hmac
import struct
import subprocess
import time

PASS_CODE_LENGTH = 6
INTERVAL = 30
ADJACENT_INTERVALS = 1
PIN_MODULO = 10**PASS_CODE_LENGTH

def get_timestamp():
    return int(time.time() / INTERVAL)

def decode_secret(secret):
    secret = secret.replace(' ', '')
    secret = secret.upper()
    secret = secret.encode('ascii')
    secret = base64.b32decode(secret)
    return secret

def make_pin(resp):
    offset = resp[-1] & 0x0F
    resp = resp[offset:offset + 4]
    pin = struct.unpack('>L', resp)[0]
    pin &= 0x7FFFFFFF
    pin %= PIN_MODULO
    return pin

def generate_challenge(secret):
    tm = get_timestamp()
    tm = struct.pack('>q', tm)

    mac = hmac.new(secret, tm, hashlib.sha1)
    resp = mac.digest()
    pin = make_pin(resp)
    print('{0:06d}'.format(pin))

def challenge_yubikey():
    tm = get_timestamp()
    tm = struct.pack('>q', tm)

    chal = binascii.hexlify(tm)
    resp = subprocess.check_output(['ykchalresp', '-2x', chal])
    resp = resp.strip()
    resp = binascii.unhexlify(resp)

    pin = make_pin(resp)
    print('{0:06d}'.format(pin))

if __name__ == "__main__":
    #secret = decode_secret(secret)
    #print(binascii.hexlify(secret))
    #generate_challenge(secret)
    challenge_yubikey()
