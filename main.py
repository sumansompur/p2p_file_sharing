from time import sleep
from server.server import main as servserv
from server.tracker import main as servtrack
from client.client import main as clcl
from client.server import main as clserv
import threading
from _thread import *


thread_lock = threading.Lock()
def main():
    start_new_thread(servserv, ())
    sleep(1)
    start_new_thread(servtrack, ())
    sleep(1)
    start_new_thread(clcl, ())
    sleep(1)
    start_new_thread(clcl, ())

    
'''Implemented Tracker
Modified server for new design
updated chunker for better working'''


if __name__ == '__main__':
    main()
