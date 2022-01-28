import os
def join_file():
    #Splits a given mp3 or video file into manageable pieces of 128Kb each for transmission through the socket. 
    CHUNK_SIZE = 1024*128+1                                                                         #Considering each file to be approx. 128Kb                                                                             #naming convention
    list = os.listdir(os.path.join(os.getcwd(), 'client','file_chunks'))
    temp = []
    for item in list:
        temp.append(int(item))
    temp.sort()
    print(temp)
    file = open(os.path.join(os.getcwd(), 'client','File', 'rcvd_file'), 'ab')
    for num in temp:
        print(num)
        temp = open(os.path.join(os.getcwd(), 'client','file_chunks', str(num)), 'rb')
        print(temp.name)
        file.write(temp.read())


    return None

#split_file('/home/sumanlokesh/GITHUB/p2p_file_sharing/Files/sample_text.txt', '/home/sumanlokesh/GITHUB/p2p_file_sharing/server/file_chunks')
if __name__ == "__main__":
    join_file()