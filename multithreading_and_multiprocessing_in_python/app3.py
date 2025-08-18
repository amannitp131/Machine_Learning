## multiprocessing 


import multiprocessing
import time

def square_numbers():
    for i in range (5):
        print(f"the square of the number {i} is {i*i}")
        time.sleep(2)


def cube_numbers():
     for i in range (5):
        print(f"the cube of the number {i} is {i*i*i}")
        time.sleep(1)


## create process 

if __name__=="__main__":
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)

    start_time=time.time()


    ##start process
    p1.start()
    p2.start()

    ## wait for process to complete 
    p1.join()
    p2.join()

    end_time=time.time()-start_time

    print(end_time)


