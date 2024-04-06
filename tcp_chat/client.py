#!/usr/bin/python3
import socket

# Machine ip address
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50050
HEADER = 64
DISCONNECT_MESSAGE = 'DISCONNECT'
FORMAT = 'utf-8'
ADDR = (HOST, PORT)

# Setting a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    "Takes a message as an argument encodes it and sends it to the server over TCP"
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

send("Hello, World!")