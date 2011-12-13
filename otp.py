#!/usr/bin/python3
################################################################################
# otp.py - Google OTP generator with secret stored on Yubikey
#
# author: mutantmonkey <mutantmonkey@mutantmonkey.in>
################################################################################

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

def make_pin(resp):
    offset = resp[-1] & 0x0F
    resp = resp[offset:offset + 4]
    pin = struct.unpack('>L', resp)[0]
    pin &= 0x7FFFFFFF
    pin %= PIN_MODULO
    return '{0:06d}'.format(pin)

def challenge_yubikey():
    tm = get_timestamp()
    tm = struct.pack('>q', tm)

    chal = binascii.hexlify(tm)
    resp = subprocess.check_output(['ykchalresp', '-2x', chal])
    resp = resp.strip()
    resp = binascii.unhexlify(resp)

    print(make_pin(resp))

if __name__ == "__main__":
    challenge_yubikey()
