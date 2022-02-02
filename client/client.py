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
            msg = msg[0:-3]
            temp = list(msg.strip("[]").split(', '))
            arr = []
            for item in temp:
                arr.append(item.strip("'"))
            peers = arr
            print('Available peers=', peers)
            time.sleep(30)

def receive():
    global file_chunk_list
    while True:
        r_client_socket = init()
        random_chunk = random.randint(0, len(file_chunk_list)-1)
        random_peer = random.randint(0, len(peers)-1)
        r_client_socket.connect((peers[random_peer], SERVER_PORT))
        r_client_socket.send(bytes(str(file_chunk_list[random_chunk]),'utf-8'))
        data = b''
        while True:
            recv = r_client_socket.recv(2080)
            data += recv
            if len(recv) == 0:
                break
        
        if data == b'file unavailable':
            continue
        else:
            print(f'Received chunk {file_chunk_list[random_chunk]} from peer_ip {peers[random_peer]}')
            myfile = open(os.path.join(os.getcwd(), 'client', 'file_chunks', str(file_chunk_list[random_chunk])), 'wb')
            myfile.write(data)
            myfile.close()
            file_chunk_list.remove(file_chunk_list[random_chunk])
            print('Remaining Chunks = ', file_chunk_list)
        
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
    print("\n\nFile Received in path below! Add extension to the received file for use")
    print(os.path.join(os.getcwd(), 'client', 'File', 'rcvd_file'))
    print("Seeding File! Press Ctrl-C to exit as a peer")
    try:
        while True:
            pass
    except KeyboardInterrupt:
            p_client_socket = init()
            p_client_socket.connect((addr, 1234))
            p_client_socket.send(bytes('bye', 'utf-8'))
            p_client_socket.close()
            for filename in os.listdir(os.path.join(os.getcwd(), 'client', 'file_chunks')):
                file_path = os.path.join(os.path.join(os.getcwd(), 'client', 'file_chunks'), filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            
        




if __name__ == '__main__':
    main()
