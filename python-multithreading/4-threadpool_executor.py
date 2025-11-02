# Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(i):
    time.sleep(1)  # Simulate a time-consuming task
    print(f"Number: {i}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(print_numbers, numbers)

    for result in results:
        print(result)  # All results are printed within the print_numbers function
