import socket
import os
import threading
from _thread import *
import random

from server.server import PORT

peers = []
file_chunk_list = []
PORT = 2300
SERVER_PORT = 2200

def init():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def peer_request(client_socket, addr):
    client_socket.connect((addr, SERVER_PORT))
    client_socket.send('hello')
    
    return None


def main():
    client = init()
    addr = input("Enter the tracker address:\n")
    start_new_thread(peer_request, (client, addr))

