"""
Real World Example: Multiprocessing for CPU Bound Tasks
Scenario: Calculating Factorials
Calculating factorials of large numbers is a CPU-bound task that requires significant computational power.
Multiprocessing can be used to distribute the computation across multiple CPU cores, significantly speeding up the process.
"""

import multiprocessing
import math
import time

def compute_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    numbers = [100000, 200000, 300000, 400000, 500000]
    t = time.time()
    
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)
    
    elapsed = time.time() - t
    print("Finished calculating factorials in ", elapsed, "seconds")
    for number, factorial in zip(numbers, results):
        print(f"Factorial of {number} has {len(str(factorial))} digits.")