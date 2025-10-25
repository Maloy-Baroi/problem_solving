"""
Array Operations - Intermediate Level

Recursive functions for intermediate-level array operations.
"""


def find_pairs_with_sum(arr, target, index=0, pairs=None, memo=None):
    """1. Find all pairs that sum to target recursively
    
    Args:
        arr (list): Input array
        target (int): Target sum
        index (int): Current index (default: 0)
        pairs (list): Found pairs (default: None)
        memo (dict): Memoization dictionary (default: None)
        
    Returns:
        list: List of tuples representing pairs that sum to target
        
    Example:
        >>> find_pairs_with_sum([1, 2, 3, 4, 5], 6)
        [(1, 5), (2, 4)]
    """
    if pairs is None:
        pairs = []
    if memo is None:
        memo = {}
    
    if index >= len(arr):
        return pairs
    
    complement = target - arr[index]
    if complement in memo:
        pairs.append((complement, arr[index]))
    
    memo[arr[index]] = index
    return find_pairs_with_sum(arr, target, index + 1, pairs, memo)


def merge_sorted_arrays(arr1, arr2, i=0, j=0):
    """3. Merge two sorted arrays recursively
    
    Args:
        arr1 (list): First sorted array
        arr2 (list): Second sorted array
        i (int): Index for first array (default: 0)
        j (int): Index for second array (default: 0)
        
    Returns:
        list: Merged sorted array
        
    Example:
        >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    if i >= len(arr1):
        return arr2[j:]
    if j >= len(arr2):
        return arr1[i:]
    
    if arr1[i] <= arr2[j]:
        return [arr1[i]] + merge_sorted_arrays(arr1, arr2, i + 1, j)
    else:
        return [arr2[j]] + merge_sorted_arrays(arr1, arr2, i, j + 1)


def binary_search_recursive(arr, target, left=0, right=None):
    """4. Implement binary search recursively
    
    Args:
        arr (list): Sorted array to search
        target: Element to find
        left (int): Left boundary (default: 0)
        right (int): Right boundary (default: None)
        
    Returns:
        int: Index of target element or -1 if not found
        
    Example:
        >>> binary_search_recursive([1, 3, 5, 7, 9, 11], 7)
        3
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def move_zeros_to_end(arr, index=0, non_zero_index=0):
    """5. Move zeros to end recursively (in-place simulation)
    
    Args:
        arr (list): Input array
        index (int): Current index (default: 0)
        non_zero_index (int): Position for next non-zero element (default: 0)
        
    Returns:
        list: Array with zeros moved to end
        
    Example:
        >>> move_zeros_to_end([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
    """
    if index >= len(arr):
        # Fill remaining positions with zeros
        while non_zero_index < len(arr):
            arr[non_zero_index] = 0
            non_zero_index += 1
        return arr
    
    if arr[index] != 0:
        if index != non_zero_index:
            arr[non_zero_index] = arr[index]
        return move_zeros_to_end(arr, index + 1, non_zero_index + 1)
    
    return move_zeros_to_end(arr, index + 1, non_zero_index)


def find_missing_number(arr, n, index=0, total_sum=None):
    """6. Find missing number in sequence 1 to n recursively
    
    Args:
        arr (list): Array with numbers from 1 to n (one missing)
        n (int): Maximum number in sequence
        index (int): Current index (default: 0)
        total_sum (int): Expected sum (default: None)
        
    Returns:
        int: Missing number
        
    Example:
        >>> find_missing_number([1, 2, 3, 5], 5)
        4
    """
    if total_sum is None:
        total_sum = n * (n + 1) // 2
    
    if index >= len(arr):
        return total_sum
    
    return find_missing_number(arr, n, index + 1, total_sum - arr[index])


def matrix_transpose_recursive(matrix, row=0, col=0, result=None):
    """7. Transpose matrix recursively
    
    Args:
        matrix (list): Input matrix (2D list)
        row (int): Current row (default: 0)
        col (int): Current column (default: 0)
        result (list): Result matrix (default: None)
        
    Returns:
        list: Transposed matrix
        
    Example:
        >>> matrix_transpose_recursive([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix:
        return []
    
    if result is None:
        # Initialize result matrix
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    
    if row >= len(matrix):
        return result
    
    if col >= len(matrix[0]):
        return matrix_transpose_recursive(matrix, row + 1, 0, result)
    
    result[col][row] = matrix[row][col]
    return matrix_transpose_recursive(matrix, row, col + 1, result)