"""
Intermediate Level Recursive Problems

This module contains intermediate-level recursive solutions for programming problems.
Functions include array manipulation, searching, and more complex operations.
"""

from .array_operations import (
    find_pairs_with_sum, merge_sorted_arrays, binary_search_recursive,
    move_zeros_to_end, find_missing_number, matrix_transpose_recursive
)
from .string_operations import first_non_repeating, one_edit_away, string_compression
from .stack_queue_operations import StackUsingQueues

__all__ = [
    # Array operations
    'find_pairs_with_sum',
    'merge_sorted_arrays',
    'binary_search_recursive',
    'move_zeros_to_end',
    'find_missing_number',
    'matrix_transpose_recursive',
    
    # String operations
    'first_non_repeating',
    'one_edit_away', 
    'string_compression',
    
    # Stack/Queue operations
    'StackUsingQueues'
]