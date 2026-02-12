"""
Climbing Stairs Problem

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 step or 2 steps.
In how many distinct ways can you climb to the top?
"""


def climb_stairs_recursive(n: int, memo: dict = None) -> int:
    """
    Recursive solution with memoization (top-down DP).
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:
        memo = {}
    
    if n <= 2:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = climb_stairs_recursive(n - 1, memo) + climb_stairs_recursive(n - 2, memo)
    return memo[n]


def climb_stairs_iterative(n: int) -> int:
    """
    Iterative solution (bottom-up DP) - Space optimized.
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    This follows the Fibonacci sequence pattern:
    - ways(1) = 1
    - ways(2) = 2
    - ways(3) = 3
    - ways(4) = 5
    - ways(5) = 8
    - etc.
    """
    if n <= 2:
        return n
    
    # We only need to keep track of the last two values
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def climb_stairs(n: int) -> int:
    """
    Main solution function (using iterative approach for efficiency).
    This is the recommended solution.
    """
    return climb_stairs_iterative(n)


# Test cases
if __name__ == "__main__":
    # Test case 1: n = 2
    result1 = climb_stairs(2)
    print(f"Input: n = 2")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print(f"✓ Correct" if result1 == 2 else "✗ Incorrect")
    print()
    
    # Test case 2: n = 3
    result2 = climb_stairs(3)
    print(f"Input: n = 3")
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print(f"✓ Correct" if result2 == 3 else "✗ Incorrect")
    print()
    
    # Additional test cases
    test_cases = [1, 4, 5, 10, 45]
    print("Additional test cases:")
    for n in test_cases:
        result = climb_stairs(n)
        print(f"n = {n}: {result} ways")
    
    # Verify both approaches give the same result
    print("\nVerifying both approaches:")
    for n in range(1, 11):
        recursive_result = climb_stairs_recursive(n)
        iterative_result = climb_stairs_iterative(n)
        match = "✓" if recursive_result == iterative_result else "✗"
        print(f"n = {n}: Recursive = {recursive_result}, Iterative = {iterative_result} {match}")
