from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(i):
    time.sleep(1)  # Simulate a time-consuming task
    return f"Number: {i}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(print_numbers, numbers)

    for result in results:
        print(result)  # Print each result returned by print_numbers function