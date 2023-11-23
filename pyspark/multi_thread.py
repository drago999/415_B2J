# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:27:36 2023

@author: GreifOfUs
"""
"""
import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
        
    return thread_local.session

def show_item(item):
    session = get_session()
    #
"""
#multi-processing: https://www.youtube.com/watch?v=GT10PnUFLlE
#multi-threading: 
import time
import multiprocessing as mp
#p1 = mp.Process(target = function_name, args = (function_arguments))
#p1.start() #starts the process
#must have no conflicting usages to maintain integrity
#not ideal for our uses

import threading
#threading.Thread(target = function_name, args = (function_args)).start()
#for item in list:
    #threading.Thread()

def helloworld():
    print("Hello world: ")

if __name__ == '__main__':
    print("start: multi_thread.py")
    #t1 = threading.Thread(target=helloworld)
    
    start = time.time()
    """
    for x in range(10):
        #t1.start() #problem calls the same thread
        threading.Thread(target=helloworld).start()
    #t1.join()
    """
    #https://stackoverflow.com/questions/22412509/getting-a-sublist-of-a-python-list-with-the-given-indices
    #shows how to get specific index... which means you can use range(lower, upper, 1)
    
    #https://stackoverflow.com/questions/33470760/python-threads-object-append-to-list
    #shows some clean up and how to keep track of threads
    
    #https://superfastpython.com/threadpoolexecutor-number-of-threads/
    #show ._max_workers
    #this shows the default thread pool in the system
    
    end = time.time()
    print("time: ",end-start)