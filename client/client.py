import socket
import os, time
import threading
from _thread import *
import random

peers = []
file_chunk_list = []
file_chunk_num = None
PORT = 2300
SERVER_PORT = 2200

def init():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def peer_request(client_socket, addr):
    global peers, file_chunk_num
    while True:
        client_socket.connect((addr, SERVER_PORT))
        client_socket.send('hello')
        msg = client_socket.recv()
        file_chunk_num = msg[-1]
        msg = msg[0:-2]
        peers = list(msg.strip('[]').split(','))
        time.sleep(30)

def receive(client_socket):
    global file_chunk_list
    while True:
        random_chunk = random.randint(1, file_chunk_num)
        random_peer = random.randint(1, len(file_chunk_list))
        client_socket.connect((peers[random_peer], SERVER_PORT))
        client_socket.send(str(random_chunk))
        data = client_socket.recv()
        if data == 'file unavailable':
            continue
        else:
            myfile = open(os.path.join(os.getcwd(), 'client', 'file_chunks', str(random_chunk), 'wb'))
            myfile.write(data)
            myfile.close()
            file_chunk_list.remove(random_chunk)
        
        if len(file_chunk_list) == 0:
            return None
            

def main():
    client = init()
    addr = input("Enter the tracker address:\n")
    a = start_new_thread(peer_request, (client, addr))
    for i in range(1, file_chunk_num+1):
        file_chunk_list.append(i)
    b = start_new_thread(receive, (client,))
    
        




if __name__ == '__main__':
    main()
