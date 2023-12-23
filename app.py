#!/usr/bin/env python3

from Tools.Banner.banner import print_banner
from Tools.C2.master import master
from Tools.C2.slave import slave
from Tools.Crypto.cryptography import crypto
from Tools.Ransom.ransomware import ransomware
from Tools.Steganography.stegano import steganography


def read_file(file):
    """Read the contents of a file and print it.

    Args:
        file (str): The name of the file to be read.
    """
    PATH = "Assets/App/"
    try:
        with open(PATH + file, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        pass

def tool():
    """Execute the tool based on user input."""
    option = get_user_input()

    if option == 1:
        clean_screen()
        read_file("Remote_Command")
        option = get_user_input()
        
        if option == 1:
            master()
            
        elif option == 2:
            slave()

        elif option == 3:
            pass

    elif option == 2:
        clean_screen()
        read_file("Cryptography")
        crypto()
    
    elif option == 3:
        clean_screen()
        read_file("Ransomware")
        ransomware()

    elif option == 4:
        clean_screen()
        read_file("Steganography")
        steganography()

    elif option == 5: 
        clean_screen()
        read_file("Contact")

    elif option == 6:
        pass


def get_user_input():
    """Prompt the user for input and return an integer."""
    option = input("xdr > ")
    return int(option)


def clean_screen():
    """Clear the console screen."""
    import os

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clean_screen()
    print_banner()
    read_file("Main")
    tool()


if __name__ == "__main__":
    main()