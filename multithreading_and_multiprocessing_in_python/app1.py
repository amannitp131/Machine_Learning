## without multithreading 

import time 

def print_number():
    for i in range(5):
        print(f"the number is {i}")
        time.sleep(2)


def print_letter():
    for letter in "abcde":
        print(f"the letter is {letter}")
        time.sleep(2)



start_time =time.time()
print_number()
print_letter()

finished_time=time.time()-start_time
print(finished_time)





