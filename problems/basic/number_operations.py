"""
Number Operations - Basic Level

Recursive functions for basic number operations.
"""


def is_palindrome_number(n, original=None, reversed_num=0):
    """2. Check if a number is palindrome recursively
    
    Args:
        n (int): Input number
        original (int): Original number (for comparison)
        reversed_num (int): Reversed number being built
        
    Returns:
        bool: True if number is palindrome, False otherwise
        
    Example:
        >>> is_palindrome_number(12321)
        True
        >>> is_palindrome_number(12345)
        False
    """
    if original is None:
        original = n
    
    if n == 0:
        return reversed_num == original
    
    reversed_num = reversed_num * 10 + n % 10
    return is_palindrome_number(n // 10, original, reversed_num)


def factorial_recursive(n):
    """5a. Find factorial recursively (already recursive by nature)
    
    Args:
        n (int): Input number
        
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial_recursive(5)
        120
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative_as_recursive(n, accumulator=1):
    """5b. Factorial using tail recursion (simulating iterative)
    
    Args:
        n (int): Input number
        accumulator (int): Accumulator for tail recursion
        
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial_iterative_as_recursive(5)
        120
    """
    if n <= 1:
        return accumulator
    return factorial_iterative_as_recursive(n - 1, accumulator * n)