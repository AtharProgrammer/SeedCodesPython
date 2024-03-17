import threading
import time
import random
from queue import Queue

queue = Queue(5)

def producer():
    while True:
        item = random.randint(1, 100)
        queue.put(item)
        print(f"Produced {item}")
        time.sleep(random.random())

def consumer():
    while True:
        item = queue.get()
        print(f"Consumed {item}")
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
