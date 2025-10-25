"""
Array Operations - Basic Level

Recursive functions for basic array operations.
"""


def find_largest(arr, index=0, max_val=float('-inf')):
    """3. Find the largest element in an array recursively
    
    Args:
        arr (list): Input array
        index (int): Current index (default: 0)
        max_val (float): Current maximum value
        
    Returns:
        int/float: Largest element in array
        
    Example:
        >>> find_largest([3, 7, 2, 9, 1])
        9
    """
    if index >= len(arr):
        return max_val
    
    max_val = max(max_val, arr[index])
    return find_largest(arr, index + 1, max_val)


def remove_duplicates(lst, index=0, seen=None):
    """6. Remove duplicates from a list recursively
    
    Args:
        lst (list): Input list
        index (int): Current index (default: 0)
        seen (set): Set of seen elements (default: None)
        
    Returns:
        list: List without duplicates
        
    Example:
        >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
        [1, 2, 3, 4, 5]
    """
    if seen is None:
        seen = set()
    
    if index >= len(lst):
        return []
    
    if lst[index] in seen:
        return remove_duplicates(lst, index + 1, seen)
    
    seen.add(lst[index])
    return [lst[index]] + remove_duplicates(lst, index + 1, seen)


def find_second_largest(arr, index=0, largest=float('-inf'), second_largest=float('-inf')):
    """9. Find second largest number in array recursively
    
    Args:
        arr (list): Input array
        index (int): Current index (default: 0)
        largest (float): Current largest value
        second_largest (float): Current second largest value
        
    Returns:
        int/float/None: Second largest element or None if not found
        
    Example:
        >>> find_second_largest([10, 20, 30, 40, 30])
        30
    """
    if index >= len(arr):
        return second_largest if second_largest != float('-inf') else None
    
    if arr[index] > largest:
        second_largest = largest
        largest = arr[index]
    elif arr[index] > second_largest and arr[index] != largest:
        second_largest = arr[index]
    
    return find_second_largest(arr, index + 1, largest, second_largest)