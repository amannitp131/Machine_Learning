import threading 
import time 
import requests
from bs4 import BeautifulSoup

urls=["https://docs.python.org/3/library/concurrent.futures.html","https://www.blackbox.ai/chat/RvO4CiA","https://chatgpt.com/c/6833dbb4-76e8-800d-820a-bd7d2c690334"]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"fetched ({len(soup.text)})")


threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("all pages fetched")