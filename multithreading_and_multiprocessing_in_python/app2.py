# with multithreading 

import threading


import time 

def print_number():
    for i in range(5):
        print(f"the number is {i}")
        time.sleep(2)


def print_letter():
    for letter in "abcde":
        print(f"the letter is {letter}")
        time.sleep(2)

## create two threads 

t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

start_time =time.time()

## start the thread
t1.start()
t2.start()

## wait for thread to complete 

t1.join()
t2.join()

finished_time=time.time()-start_time
print(finished_time)





