from re import I
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

def send_data(conn_socket, addr):
    file_no = str(conn_socket.recv(1024), 'utf-8')
    print('Sending file_chunk', file_no, "to", addr[0])
    myfile = open(os.path.join(os.getcwd(), 'server', 'file_chunks', file_no), 'rb')
    while True:
        pkt = myfile.read(2080)
        if len(pkt) > 0:
            conn_socket.send(pkt)
        else:
            break

    conn_socket.close()
    return None

def main():
    try:
        server = init()
        path = input("Enter the absolute file path\n")
        source_path = os.path.join(os.getcwd(), 'server', 'send_samples', os.path.basename(path))
        dest_path = os.path.join(os.getcwd(), 'server', 'file_chunks')
        shutil.copy(path, source_path)
        chunker.split_file(source_path, dest_path)
        print("Ready to serve")
        while True:
            sock_obj, addr = server.accept()
            start_new_thread(send_data, (sock_obj, addr))
    except KeyboardInterrupt:
        server.close()




if __name__ == '__main__':
    main()