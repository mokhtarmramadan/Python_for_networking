#!/usr/bin/python3
''' Script to make the server listen on it's own ip4 addres port 50050 '''
import threading
import socket
import time

# Machine ip address
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50050
HEADER = 64
DISCONNECT_MESSAGE = 'DISCONNECT'
# Socket object that with AF_INET address family and SOCK_STREAM as a socket type 
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (HOST, PORT)
SERVER.bind(ADDR)

def handle_client(conn, addr):
    ''' Handles threads untill the msg is `DISCONNECT` '''

    print("[NEW CONNECTION] {} CONNECTED".format(addr))
    connected = True

    while connected:
        msg_len = conn.recv(HEADER).decode('utf-8')
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(HEADER).decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print("[{}] - {}".format(addr, msg))
    conn.close()


def start():
    ''' Start listening and creates a thread to handle each and every new connection'''
    SERVER.listen()
    print("Listening on {}".format(SERVER))
    while True:
        conn, addr = SERVER.accept()
        t1 = threading.Thread(target=handle_client, args=(conn, addr))
        t1.start()
        print('[ACTIVE CONNETIONS] {}'.format(threading.active_count() - 1))


print("Starting the connection.....")
start()