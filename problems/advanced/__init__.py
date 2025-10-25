"""
Advanced Level Recursive Problems

This module contains advanced-level recursive solutions for complex programming problems.
Includes algorithms, data structures, and advanced problem-solving techniques.
"""

from .string_operations import longest_substring_no_repeat
from .linked_list_operations import detect_cycle_recursive
from .cache_operations import LRUCache
from .array_operations import (
    merge_intervals_recursive, kadane_recursive, 
    trap_rain_water_recursive, find_kth_largest
)
from .tree_operations import max_depth_binary_tree
from .backtracking_operations import combination_sum_recursive

__all__ = [
    # String operations
    'longest_substring_no_repeat',
    
    # Linked list operations
    'detect_cycle_recursive',
    
    # Cache operations
    'LRUCache',
    
    # Array operations
    'merge_intervals_recursive',
    'kadane_recursive',
    'trap_rain_water_recursive', 
    'find_kth_largest',
    
    # Tree operations
    'max_depth_binary_tree',
    
    # Backtracking operations
    'combination_sum_recursive'
]