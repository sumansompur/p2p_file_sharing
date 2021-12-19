import chunker

def send_data(path):
    chunker.split_file(path, '/home/sumanlokesh/GITHUB/p2p_file_sharing/server/file_chunks')
    return None