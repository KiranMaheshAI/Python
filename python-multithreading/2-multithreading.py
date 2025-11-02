# Multithreading in Python allows multiple threads to run concurrently within a single process. 
# This is useful for I/O-bound tasks where threads can wait for external resources without blocking the entire program like File Operations, network requests.
#  Concurrent execution: when you want to improve the throughput of your application  by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Number: {i}")


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.5)  # Simulate a time-consuming task
        print(f"Letter: {letter}")

if __name__ == "__main__":
    t = time.time()
    # Create threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    elapsed = time.time() - t
    print("Finished printing numbers and letters in ", elapsed, "seconds")