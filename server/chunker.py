
def split_file(source_path, dest_path):
    #Splits a given mp3 or video file into manageable pieces of 128Kb each for transmission through the socket. 
    CHUNK_SIZE = 1024*128                                                                           #Considering each file to be approx. 128Kb
    file_number = 1                                                                                 #naming convention
    with open(source_path, 'rb') as f:                                                              #open source file in binary read mode
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            if source_path.endswith('.mp3'):
                dest_name = '/audio/my_song_part_'
            elif source_path.endswith('.txt'):
                dest_name = '/text/my_text_part_'
            elif source_path.endswith('.mp4'):
                dest_name = '/video/my_video_part_'
                 
            with open(dest_path + dest_name + str(file_number), 'wb') as chunk_file:
                chunk_file.write(chunk)                                                             #create and write bin files containing file data
            file_number += 1                
            chunk = f.read(CHUNK_SIZE)
    return None

#split_file('/home/sumanlokesh/GITHUB/p2p_file_sharing/server/send_samples/sample_text.txt', '/home/sumanlokesh/GITHUB/p2p_file_sharing/server/file_chunks')
