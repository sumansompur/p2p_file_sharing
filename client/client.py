from encodings import utf_8
import socket
import os, time
import threading
from _thread import *
import random
import chunker

peers = []
file_chunk_list = []
file_chunk_num = None
PORT = 2300
SERVER_PORT = 2200

def init():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def peer_request(addr):
    global peers, file_chunk_num
    while True:
        p_client_socket = init()
        p_client_socket.connect((addr, 1234))
        p_client_socket.send(bytes('hello', 'utf-8'))
        msg = str(p_client_socket.recv(1024), 'utf-8')
        print(msg)
        if file_chunk_num == None:
            file_chunk_num = int(msg[-2] + msg[-1])
        print(msg)
        msg = msg[0:-3]
        print(msg)
        temp = list(msg.strip("[]").split(', '))
        for item in temp:
            peers.append(item.strip("'"))
        print(peers)
        time.sleep(30)

def receive():
    global file_chunk_list
    while True:
        r_client_socket = init()
        random_chunk = random.randint(0, len(file_chunk_list)-1)
        print(random_chunk)
        random_peer = random.randint(0, len(peers)-1)
        print(random_peer)
        r_client_socket.connect((peers[random_peer], SERVER_PORT))
        r_client_socket.send(bytes(str(file_chunk_list[random_chunk]),'utf-8'))
        data = r_client_socket.recv(1024*128)
        msg = None
        try:
            msg = str(data, 'utf-8')
        except:
            pass
        if msg == 'file unavailable':
            continue
        else:
            myfile = open(os.path.join(os.getcwd(), 'client', 'file_chunks', str(file_chunk_list[random_chunk])), 'wb')
            myfile.write(data)
            myfile.close()
            file_chunk_list.remove(file_chunk_list[random_chunk])
            print(file_chunk_list)
        
        r_client_socket.close()
        if len(file_chunk_list) == 0:
            chunker.join_file()
            return None
            

def main():
    addr = input("Enter the tracker address:\n")
    a = start_new_thread(peer_request, (addr,))
    time.sleep(2)
    for i in range(1, file_chunk_num+1):
        file_chunk_list.append(i)
    print(file_chunk_list)
    receive()
    print("File Received! Add extension to the received file for use")
    
        




if __name__ == '__main__':
    main()
