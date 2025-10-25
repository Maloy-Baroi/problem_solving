"""
Test Suite for Advanced Level Problems

Tests for all advanced level recursive functions.
"""

from problems.advanced import (
    longest_substring_no_repeat, detect_cycle_recursive, LRUCache,
    merge_intervals_recursive, kadane_recursive, trap_rain_water_recursive,
    find_kth_largest, max_depth_binary_tree, combination_sum_recursive
)
from algorithms import quicksort, mergesort
from data_structures import ListNode, TreeNode


def test_advanced_functions():
    """Test all advanced level functions"""
    print("\n" + "=" * 50)
    print("TESTING ADVANCED LEVEL FUNCTIONS")
    print("=" * 50)
    
    # 1. Longest substring
    print("1. Longest substring without repeat in 'abcabcbb':", 
          longest_substring_no_repeat("abcabcbb"))
    
    # 2. Cycle detection (create a simple linked list with cycle)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Create cycle
    print("2. Cycle in linked list?", detect_cycle_recursive(node1))
    
    # 3. LRU Cache
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print("3. LRU Cache: put(1,1), put(2,2), get(1):", lru.get(1))
    lru.put(3, 3)  # Evicts key 2
    print("   After put(3,3), get(2):", lru.get(2))  # Returns -1
    
    # 4. Merge intervals
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("4. Merge intervals [[1,3],[2,6],[8,10],[15,18]]:", 
          merge_intervals_recursive(intervals))
    
    # 5. Maximum subarray sum
    print("5. Max subarray sum in [-2,1,-3,4,-1,2,1,-5,4]:", 
          kadane_recursive([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    
    # 6. Sorting
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"6a. Quicksort {arr}:", quicksort(arr))
    print(f"6b. Mergesort {arr}:", mergesort(arr))
    
    # 7. Trapping rain water
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("7. Trapped rain water:", trap_rain_water_recursive(height))
    
    # 8. Kth largest
    arr = [3, 2, 1, 5, 6, 4]
    print(f"8. 2nd largest in {arr}:", find_kth_largest(arr, 2))
    
    # 9. Binary tree max depth
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("9. Max depth of binary tree:", max_depth_binary_tree(root))
    
    # 10. Combination sum
    print("10. Combinations of [2,3,6,7] that sum to 7:", 
          combination_sum_recursive([2, 3, 6, 7], 7))