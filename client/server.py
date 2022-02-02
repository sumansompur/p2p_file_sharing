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
    print('Trying to send file_chunk ', file_no)
    try:
        myfile = open(os.path.join(os.getcwd(), 'client', 'file_chunks', file_no), 'rb')
        while True:
            pkt = myfile.read(2080)
            if len(pkt) > 0:
                conn_socket.send(pkt)
            else:
                break
    except:
        print('File Chunk unavailabale')
        conn_socket.send(b'file unavailable')
    
    conn_socket.close()
    return None

def main():
    try:
        server = init()
        while True:
            sock_obj, addr = server.accept()
            start_new_thread(send_data, (sock_obj,))
    except KeyboardInterrupt:
        server.close()
        exit(0)






if __name__ == '__main__':
    main()