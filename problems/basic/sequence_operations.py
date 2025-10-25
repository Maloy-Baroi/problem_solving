"""
Sequence Operations - Basic Level

Recursive functions for sequence generation and operations.
"""


def fibonacci_sequence(n, a=0, b=1, result=None):
    """8. Print Fibonacci sequence up to n terms recursively
    
    Args:
        n (int): Number of terms to generate
        a (int): First number (default: 0)
        b (int): Second number (default: 1) 
        result (list): Result list (default: None)
        
    Returns:
        list: List of Fibonacci numbers
        
    Example:
        >>> fibonacci_sequence(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if result is None:
        result = []
    
    if n <= 0:
        return result
    
    result.append(a)
    return fibonacci_sequence(n - 1, b, a + b, result)