# In Multiprocessing, processes run in parallel.
# Each process has its own Python interpreter and memory space, which allows true parallelism, especially for CPU-bound tasks like heavy mathematical computations, data analysis.
import multiprocessing
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
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for both processes to complete
    process1.join()
    process2.join()
    elapsed = time.time() - t
    print("Finished printing numbers and letters in ", elapsed, "seconds")