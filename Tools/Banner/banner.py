#!/usr/bin/env python3

import random
import os


PATH = "Assets/Banner"

def print_banner():
    banner_file = get_banner()
    with open(f"{PATH}/{banner_file}") as f:    
        print(f.read())

def get_banner():
    banner_list = os.listdir(PATH)
    banner_file = random.choice(banner_list)
    return banner_file


        