"""
Array Operations - Advanced Level

Advanced recursive functions for complex array operations.
"""


def merge_intervals_recursive(intervals, index=0, merged=None):
    """4. Merge overlapping intervals recursively
    
    Args:
        intervals (list): List of intervals [start, end]
        index (int): Current index (default: 0)
        merged (list): List of merged intervals (default: None)
        
    Returns:
        list: List of merged intervals
        
    Example:
        >>> merge_intervals_recursive([[1,3],[2,6],[8,10],[15,18]])
        [[1, 6], [8, 10], [15, 18]]
    """
    if merged is None:
        intervals.sort(key=lambda x: x[0])
        merged = []
    
    if index >= len(intervals):
        return merged
    
    if not merged or merged[-1][1] < intervals[index][0]:
        merged.append(intervals[index])
    else:
        merged[-1][1] = max(merged[-1][1], intervals[index][1])
    
    return merge_intervals_recursive(intervals, index + 1, merged)


def kadane_recursive(arr, index=0, max_ending_here=0, max_so_far=float('-inf')):
    """5. Maximum sum subarray using Kadane's algorithm recursively
    
    Args:
        arr (list): Input array
        index (int): Current index (default: 0)
        max_ending_here (int): Maximum sum ending at current position (default: 0)
        max_so_far (int): Maximum sum found so far (default: -inf)
        
    Returns:
        int: Maximum sum of contiguous subarray
        
    Example:
        >>> kadane_recursive([-2,1,-3,4,-1,2,1,-5,4])
        6
    """
    if index >= len(arr):
        return max_so_far
    
    max_ending_here = max(arr[index], max_ending_here + arr[index])
    max_so_far = max(max_so_far, max_ending_here)
    
    return kadane_recursive(arr, index + 1, max_ending_here, max_so_far)


def trap_rain_water_recursive(height, left=0, right=None, left_max=0, right_max=0):
    """7. Trapping rain water problem recursively
    
    Args:
        height (list): Array of heights
        left (int): Left pointer (default: 0)
        right (int): Right pointer (default: None)
        left_max (int): Maximum height seen from left (default: 0)
        right_max (int): Maximum height seen from right (default: 0)
        
    Returns:
        int: Total water trapped
        
    Example:
        >>> trap_rain_water_recursive([0,1,0,2,1,0,1,3,2,1,2,1])
        6
    """
    if right is None:
        right = len(height) - 1
    
    if left >= right:
        return 0
    
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
            return trap_rain_water_recursive(height, left + 1, right, left_max, right_max)
        else:
            water = left_max - height[left]
            return water + trap_rain_water_recursive(height, left + 1, right, left_max, right_max)
    else:
        if height[right] >= right_max:
            right_max = height[right]
            return trap_rain_water_recursive(height, left, right - 1, left_max, right_max)
        else:
            water = right_max - height[right]
            return water + trap_rain_water_recursive(height, left, right - 1, left_max, right_max)


def partition(arr, left, right, k):
    """Helper for finding kth largest using quickselect
    
    Args:
        arr (list): Input array
        left (int): Left boundary
        right (int): Right boundary  
        k (int): Kth position to find
        
    Returns:
        int: Kth largest element
    """
    pivot_index = left
    pivot = arr[right]
    
    for i in range(left, right):
        if arr[i] >= pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    if pivot_index == k - 1:
        return arr[pivot_index]
    elif pivot_index > k - 1:
        return partition(arr, left, pivot_index - 1, k)
    else:
        return partition(arr, pivot_index + 1, right, k)


def find_kth_largest(arr, k):
    """8. Find kth largest element recursively using quickselect
    
    Args:
        arr (list): Input array
        k (int): Kth position (1-indexed)
        
    Returns:
        int/None: Kth largest element or None if invalid input
        
    Example:
        >>> find_kth_largest([3,2,1,5,6,4], 2)
        5
    """
    if not arr or k <= 0 or k > len(arr):
        return None
    
    return partition(arr.copy(), 0, len(arr) - 1, k)