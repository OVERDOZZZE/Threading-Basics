import threading
import time
import requests

# Program 1 (lvl.1)

def print_text(thr_num, delay):
    time.sleep(delay)
    print(f'Hello from thread number {thr_num}\n')

t1 = threading.Thread(target=print_text, args=(1,1))
t2 = threading.Thread(target=print_text, args=(2,2))
t3 = threading.Thread(target=print_text, args=(3,3))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# Program 1 (lvl.1) --- Remake

threads = []

for i in range(1,4):
    t = threading.Thread(target=print_text, args=(i, i))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

# Program 2 (lvl.2) 

urls = ['url/1', 'url/2', 'url/3', 'url/4', 'url/5']

def downloader(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        filename = 'photo_' + url.split('/')[-1]

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024*1024):
                file.write(chunk)
    except Exception as e:
        print(f'Failed to download url {url}: {e}')

threads = []

for url in urls:
    t = threading.Thread(target=downloader, args=(url,))
    threads.append(t)
    t.start()
            
for t in threads:
    t.join()

print("All threads joined. Some files may have failed. Check logs above.")

# Program 3 (lvl.2.5)

import random
import threading
from pathlib import Path
import time
import logging


log_file = Path.home() / 'OneDrive' / 'Рабочий стол' /'log_file.txt'

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info('Start of the program')

def data_processing(delay, lock):
    thread_name = threading.current_thread().name

    try:
        time.sleep(delay)
        with lock:
            logger.info(f'{thread_name} finished processing of element N')

    except Exception as e:
        logger.error(f'Error {e} occured at thread: {thread_name}')


threads = []    
lock = threading.Lock()

for _ in range(10):
    t = threading.Thread(target=data_processing, args=(random.randint(1, 5), lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

logger.info('Joins\' were executed')

# comments 
