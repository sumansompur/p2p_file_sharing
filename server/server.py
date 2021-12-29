import chunker
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
    
    return None


def main():
    server = init()
    path = input("Enter the absolute file path")
    source_path = os.path.join(os.getcwd(), 'server', 'send_samples', os.path.basename(path))
    dest_path = os.path.join(os.getcwd(), 'server', 'file_chunks')
    shutil.copy(path, source_path)
    chunker.split_file(source_path, dest_path)
    while True:
        sock_obj, addr = server.accept()
        thread_lock.acquire()
        start_new_thread(send_data, (sock_obj,))







if __name__ == '__main__':
    main()