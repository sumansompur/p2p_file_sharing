import socket
import os, shutil
import threading
from _thread import *

thread_lock = threading.Lock()
PORT = 2200

def init():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(5)
    return server_socket

def send_data(conn_socket):
    file_no = str(conn_socket.recv(1024), 'utf-8')
    try:
        myfile = open(os.path.join(os.getcwd(), 'client', 'file_chunks', file_no), 'rb')
        conn_socket.send(myfile.read(1024*128))
        conn_socket.close()
    except:
        conn_socket.send(bytes('file unavailable', 'utf-8'))
    return None

def main():
    server = init()
    while True:
        sock_obj, addr = server.accept()
        start_new_thread(send_data, (sock_obj,))






if __name__ == '__main__':
    main()