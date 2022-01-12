import socket
import threading
from _thread import *
import os

thread_lock = threading.Lock()
SOCKET_PORT = 1234
active = []

def file_chunk_nos():
    list = os.listdir(os.path.join(os.getcwd(), 'server','file_chunks'))
    return len(list)
    
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('100.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def init():
    tracker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tracker_socket.bind(('0.0.0.0', SOCKET_PORT))
    hostip = get_ip()
    global active
    active.append(hostip)
    tracker_socket.listen(5)
    return tracker_socket

def send_info(conn_sock, addr):
    C_ip = conn_sock.recv(1024)
    global active
    if C_ip.lower() == 'bye':
        active.remove(addr[0])
        conn_sock.send('bye')
    else:
        send_message = str(active) + ',' + str(file_chunk_nos())
        conn_sock.send(send_message)
        active.append(addr[0])
        conn_sock.close()
        return None


def main():
    tracker = init()
    global active
    while True:
        conn_sock, addr = tracker.accept()
        start_new_thread(send_info, (conn_sock, addr))





if __name__ == '__main__':
    main()
