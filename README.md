# yubikey-googleauth

*Note: ykchalresp has added integrated OATH-TOTP functionality, so you no longer need to use otp.py. The get_secret.py tool is still useful, however.*

Google Authenticator is great, but I don't really want to be tied to my mobile
phone for logging into Google Services. Yubikey is the ideal form factor for a
two-factor authentication device, so why not integrate the two? Well now, you
can!

This code is primarily a proof of concept at the current time and although
functional, requires some manual interaction to get started.

Available under the ISC License.

## Prerequisites
* Python 3.x
* ykchalresp (found in the yubikey-personalization package)

## Usage
1. Set up Google Authenticator on your Google settings like you would for a
   mobile phone.
2. Below the QR code, press the expand button so you can see your base32-encoded
   secret key.
3. Run `get_secret.py`; this will prompt you for your base32-encoded secret and
   output a result in hex.
4. Program that secret into your Yubikey as a HMAC-SHA1 challenge-response key.
   `ykpersonalize -2 -o chal-resp -o chal-hmac -o hmac-lt64 -a <the secret key>`
5. Whenever you are prompted for a one-time password from Google, just run
   `otp.py` and the output will be a one-time password usable for up to one
   minute 30 seconds.
