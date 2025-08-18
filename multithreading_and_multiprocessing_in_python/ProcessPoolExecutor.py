from concurrent.futures import ProcessPoolExecutor
import time

def isPrime(n):
    time.sleep(5)
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    


if __name__=="__main__":
    numbers = [i for i in range (1,5)]

    start = time.time()
    for number in numbers:
        isPrime(number)
    print(f"Time without multiprocessing: {time.time() - start:.2f}s")

    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(isPrime, numbers))
    print(f"Time with multiprocessing: {time.time() - start:.2f}s")

## output-> 
## note ->Time without multiprocessing: 20.00s
# Time with multiprocessing: 5.17s
