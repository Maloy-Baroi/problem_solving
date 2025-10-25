"""
Test Suite for Intermediate Level Problems

Tests for all intermediate level recursive functions.
"""

from problems.intermediate import (
    find_pairs_with_sum, first_non_repeating, merge_sorted_arrays,
    binary_search_recursive, move_zeros_to_end, find_missing_number,
    matrix_transpose_recursive, one_edit_away, string_compression,
    StackUsingQueues
)


def test_intermediate_functions():
    """Test all intermediate level functions"""
    print("\n" + "=" * 50)
    print("TESTING INTERMEDIATE LEVEL FUNCTIONS")
    print("=" * 50)
    
    # 1. Pairs with sum
    print("1. Pairs in [1,2,3,4,5] that sum to 6:", find_pairs_with_sum([1, 2, 3, 4, 5], 6))
    
    # 2. First non-repeating
    print("2. First non-repeating in 'leetcode':", first_non_repeating("leetcode"))
    
    # 3. Merge sorted arrays
    print("3. Merge [1,3,5] and [2,4,6]:", merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
    
    # 4. Binary search
    arr = [1, 3, 5, 7, 9, 11]
    print(f"4. Binary search for 7 in {arr}:", binary_search_recursive(arr, 7))
    
    # 5. Move zeros
    arr = [0, 1, 0, 3, 12]
    print(f"5. Move zeros in {arr}:", move_zeros_to_end(arr.copy()))
    
    # 6. Missing number
    print("6. Missing number in [1,2,3,5] (n=5):", find_missing_number([1, 2, 3, 5], 5))
    
    # 7. Matrix transpose
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("7. Transpose of [[1,2,3],[4,5,6]]:", matrix_transpose_recursive(matrix))
    
    # 8. One edit away
    print("8. Are 'pale' and 'ple' one edit away?", one_edit_away("pale", "ple"))
    
    # 9. String compression
    print("9. Compress 'aaabbbc':", string_compression("aaabbbc"))
    
    # 10. Stack using queues
    stack = StackUsingQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("10. Stack operations: pushed 1,2,3")
    print("    Pop:", stack.pop())
    print("    Top:", stack.top())