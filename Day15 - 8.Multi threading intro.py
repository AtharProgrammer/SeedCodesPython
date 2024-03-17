'''
Multithreading in Python allows you to execute multiple threads (lightweight processes) concurrently within a single process.
This can be useful for tasks like parallelizing I/O-bound operations or improving the responsiveness of a GUI application.
Below is a basic tutorial on multithreading in Python:

1. **Importing the `threading` Module**: Python's `threading` module provides support for creating and managing threads.

'''
import threading

'''
2. **Creating a Thread**: You can create a thread by subclassing the `threading.Thread` class and overriding the `run()` method with the
code you want to execute in the thread.
'''

class MyThread(threading.Thread):
    def run(self):
        # Code to be executed in the thread
        print("Hello from a thread!")

# Create an instance of the thread
my_thread = MyThread()

# Start the thread
my_thread.start()


'''
3. **Using the `target` Argument**: Alternatively, you can create a thread by passing a target function to the `Thread` constructor.

'''
def my_function():
    # Code to be executed in the thread
    print("Hello from a thread!")

# Create a thread with a target function
my_thread = threading.Thread(target=my_function)

# Start the thread
my_thread.start()

'''
4. **Joining Threads**: You can use the `join()` method to wait for a thread to complete before continuing execution.

'''
# Wait for the thread to finish
my_thread.join()

print("Thread execution complete!")

'''

5. **Passing Arguments to Threads**: You can pass arguments to a thread by specifying them in the `args` parameter.

'''
def greet(name):
    print(f"Hello, {name}!")

# Create a thread with arguments
my_thread = threading.Thread(target=greet, args=("Alice",))

# Start the thread
my_thread.start()

'''
6. **Thread Synchronization**: When multiple threads access shared resources, you may need to use synchronization mechanisms
like locks to prevent race conditions.

'''
lock = threading.Lock()

def increment(counter):
    for _ in range(1000):
        # Acquire the lock before updating the counter
        with lock:
            counter += 1

counter = 0
threads = []

# Create multiple threads to increment the counter
for _ in range(10):
    thread = threading.Thread(target=increment, args=(counter,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Counter:", counter)

'''
This is a basic introduction to multithreading in Python using the `threading` module.
There are also advanced topics like thread pools, thread synchronization, and thread safety that you can explore as
you become more familiar with multithreading concepts.
'''
