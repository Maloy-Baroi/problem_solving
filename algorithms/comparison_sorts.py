"""
Comparison-based Sorting Algorithms

Recursive implementations of comparison-based sorting algorithms.
"""


def quicksort(arr):
    """6a. Quicksort recursively
    
    Sorts an array using the quicksort algorithm with recursive partitioning.
    
    Args:
        arr (list): Array to sort
        
    Returns:
        list: Sorted array
        
    Example:
        >>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) average
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


def merge(left, right):
    """Helper for mergesort - merges two sorted arrays
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
        
    Returns:
        list: Merged sorted array
        
    Example:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    
    if left[0] <= right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def mergesort(arr):
    """6b. Mergesort recursively
    
    Sorts an array using the mergesort algorithm with recursive divide-and-conquer.
    
    Args:
        arr (list): Array to sort
        
    Returns:
        list: Sorted array
        
    Example:
        >>> mergesort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)