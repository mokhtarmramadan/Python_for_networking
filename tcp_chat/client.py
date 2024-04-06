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
    pass