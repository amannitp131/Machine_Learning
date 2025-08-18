# real world use cases->
# suppose we are given a list of numbers and each number have very large value
# and i have to calculate the factorail of each number which will take a lot of time if we do it with singe core CPU

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import time 
import math


def calculate_factoraial(num):
    result=math.factorial(num)
    print(f"the factorial of the number {num} is {result}")


if __name__=="__main__":
    numbers=[100,1000,800,900,700]
    start_time=time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        result=executor.map(calculate_factoraial,numbers)

    end_time=time.time()

    print(f"results: ",{result})
    print(f"time taken ={end_time-start_time}")
    