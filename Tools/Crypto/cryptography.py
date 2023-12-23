#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os.path

PATH = "Assets/Ransomware/"
KEY = "key.key"


def generate_key():
    key = Fernet.generate_key()
    
    with open(PATH + KEY, 'wb') as write_key:
        write_key.write(key)


def load_key():
    if not os.path.exists(PATH + KEY):
        generate_key()
    
    with open(PATH + KEY, 'rb') as r:
        return r.read()


def read_file():
    file_name = input("Filename : ")
    
    with open(PATH + file_name, "rb") as file:
        return file_name, file.read()


def encrypt_file():
    key = load_key()
    fernet = Fernet(key)
    file_name, file_data = read_file()

    encrypted_file = fernet.encrypt(file_data)
    with open(f"{PATH}{file_name}", 'wb') as w:
        w.write(encrypted_file)


def decrypt_file():
    key = load_key()
    fernet = Fernet(key)
    file_name, file_data = read_file()
    decrypted_file = fernet.decrypt(file_data)

    with open(f"{PATH}decrypted_{file_name}", 'wb') as w:
        w.write(decrypted_file)


def crypto():
    option = input("xdr > ")
    option = int(option.strip())

    if option == 1:
        encrypt_file()  

    elif option == 2:
        decrypt_file()

    elif option == 3:
        encrypt_file()
        decrypt_file()
    else:
        pass
