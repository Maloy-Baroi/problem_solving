"""
Backtracking Operations - Advanced Level

Advanced recursive functions using backtracking techniques.
"""


def combination_sum_recursive(candidates, target, start=0, current=None, result=None):
    """10. Find all combinations that sum to target using backtracking
    
    Args:
        candidates (list): List of candidate numbers
        target (int): Target sum
        start (int): Starting index (default: 0)
        current (list): Current combination being built (default: None)
        result (list): List of all valid combinations (default: None)
        
    Returns:
        list: List of all combinations that sum to target
        
    Example:
        >>> combination_sum_recursive([2,3,6,7], 7)
        [[2, 2, 3], [7]]
    """
    if current is None:
        current = []
    if result is None:
        result = []
    
    if target == 0:
        result.append(current.copy())
        return result
    
    if target < 0 or start >= len(candidates):
        return result
    
    # Include current element (can be used multiple times)
    current.append(candidates[start])
    combination_sum_recursive(candidates, target - candidates[start], start, current, result)
    current.pop()
    
    # Exclude current element and move to next
    combination_sum_recursive(candidates, target, start + 1, current, result)
    
    return result