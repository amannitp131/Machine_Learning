from concurrent.futures import ThreadPoolExecutor
import time 


def print_numbers(number):
    
    print(number)
    time.sleep(5)



if __name__=="__main__":
    numbers=[1,2,3,4,5,6,7,8,9,10]
    with ThreadPoolExecutor(max_workers=2) as executor:
        results=executor.map(print_numbers,numbers)

    for result in results:
        print(result)
    














