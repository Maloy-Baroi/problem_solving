# Recursive Solutions - Complete Implementation Guide

## Overview
This repository contains recursive implementations for 30 programming problems across three difficulty levels. Every solution uses recursion as the primary problem-solving approach.

## Key Recursive Patterns Used

### 1. **Base Case + Recursive Case**
The fundamental pattern where we define stopping conditions and recursive calls.

### 2. **Accumulator Pattern**
Passing accumulated results through recursive calls (e.g., factorial, string building).

### 3. **Divide and Conquer**
Breaking problems into smaller subproblems (e.g., binary search, merge sort, quicksort).

### 4. **Backtracking**
Exploring all possibilities and undoing choices (e.g., combination sum).

### 5. **Tail Recursion**
Optimized recursion where the recursive call is the last operation.

### 6. **Helper Function Recursion**
Using helper functions with additional parameters to maintain state.

## Basic Level Solutions (1-10)

### 1. **String Reversal**
- **Pattern**: Simple recursion
- **Approach**: Take last character + reverse of remaining string

### 2. **Palindrome Number**
- **Pattern**: Helper with accumulator
- **Approach**: Build reversed number recursively and compare

### 3. **Find Largest Element**
- **Pattern**: Linear recursion with accumulator
- **Approach**: Track maximum while traversing

### 4. **Count Vowels**
- **Pattern**: Count and recurse
- **Approach**: Check current character and add to recursive count

### 5. **Factorial (Two Versions)**
- **Pattern**: Classic recursion & tail recursion
- **Approach**: Multiply n by factorial(n-1) OR use accumulator

### 6. **Remove Duplicates**
- **Pattern**: Filter with state tracking
- **Approach**: Use set to track seen elements

### 7. **Check Anagrams**
- **Pattern**: Character matching with recursion
- **Approach**: Match and remove characters recursively

### 8. **Fibonacci Sequence**
- **Pattern**: Dual accumulator
- **Approach**: Track two previous values

### 9. **Second Largest**
- **Pattern**: Dual tracking
- **Approach**: Maintain largest and second largest

### 10. **Unique Characters**
- **Pattern**: Set-based tracking
- **Approach**: Check for duplicates using set

## Intermediate Level Solutions (1-10)

### 1. **Find Pairs with Sum**
- **Pattern**: Hash table with recursion
- **Approach**: Track complements in dictionary

### 2. **First Non-Repeating Character**
- **Pattern**: Two-pass recursion
- **Approach**: Count first, then find first with count=1

### 3. **Merge Sorted Arrays**
- **Pattern**: Two-pointer recursion
- **Approach**: Compare heads and recurse on remainder

### 4. **Binary Search**
- **Pattern**: Divide and conquer
- **Approach**: Eliminate half of search space each call

### 5. **Move Zeros to End**
- **Pattern**: In-place modification with tracking
- **Approach**: Track non-zero position while traversing

### 6. **Find Missing Number**
- **Pattern**: Mathematical recursion
- **Approach**: Subtract from expected sum

### 7. **Matrix Transpose**
- **Pattern**: 2D recursion
- **Approach**: Process row by row, column by column

### 8. **One Edit Away**
- **Pattern**: Multiple branch recursion
- **Approach**: Try all edit operations recursively

### 9. **String Compression**
- **Pattern**: Run-length encoding
- **Approach**: Count consecutive characters

### 10. **Stack Using Queues**
- **Pattern**: Recursive queue operations
- **Approach**: Recursively move elements between queues

## Advanced Level Solutions (1-10)

### 1. **Longest Substring Without Repeats**
- **Pattern**: Sliding window recursion
- **Approach**: Expand window or shrink from start

### 2. **Detect Cycle in Linked List**
- **Pattern**: Floyd's algorithm recursively
- **Approach**: Fast and slow pointer technique

### 3. **LRU Cache**
- **Pattern**: Recursive list operations
- **Approach**: Recursively manage order list

### 4. **Merge Overlapping Intervals**
- **Pattern**: Sorted recursion
- **Approach**: Sort then merge recursively

### 5. **Maximum Subarray (Kadane's)**
- **Pattern**: Dynamic programming recursion
- **Approach**: Track max ending at each position

### 6. **Quicksort & Mergesort**
- **Pattern**: Divide and conquer
- **Approach**: Partition/split, sort recursively, combine

### 7. **Trapping Rain Water**
- **Pattern**: Two-pointer recursion
- **Approach**: Process from both ends based on height

### 8. **Kth Largest (Quickselect)**
- **Pattern**: Partial sorting recursion
- **Approach**: Partition and recurse on relevant half

### 9. **Binary Tree Max Depth**
- **Pattern**: Tree recursion
- **Approach**: 1 + max(left_depth, right_depth)

### 10. **Combination Sum**
- **Pattern**: Backtracking
- **Approach**: Include/exclude current element

## Time & Space Complexity Analysis

### Basic Level
- Most solutions: O(n) time, O(n) space (call stack)
- Factorial: O(n) time, O(n) space
- Anagrams: O(n²) time worst case

### Intermediate Level
- Binary Search: O(log n) time, O(log n) space
- Merge Arrays: O(m+n) time, O(m+n) space
- Matrix Transpose: O(m×n) time and space
- String Compression: O(n) time and space

### Advanced Level
- Sorting algorithms: O(n log n) average time
- Quickselect: O(n) average, O(n²) worst case
- LRU Cache: O(n) for removal operations
- Combination Sum: O(2^n) time complexity

## Key Recursion Optimization Techniques

### 1. **Tail Recursion**
- Last operation is recursive call
- Can be optimized by compilers
- Example: Tail recursive factorial

### 2. **Memoization**
- Cache results of expensive calls
- Trade space for time
- Useful for overlapping subproblems

### 3. **Accumulator Pattern**
- Pass partial results as parameters
- Reduces need for combining results
- Example: String building, sum accumulation

### 4. **Early Termination**
- Return as soon as answer is found
- Avoid unnecessary recursive calls
- Example: Binary search, quickselect

## Common Pitfalls & Solutions

### 1. **Stack Overflow**
- **Problem**: Deep recursion exceeds stack limit
- **Solution**: Use iterative approach for large inputs or increase stack size

### 2. **Redundant Computation**
- **Problem**: Recalculating same values
- **Solution**: Memoization or dynamic programming

### 3. **Mutable Default Arguments**
- **Problem**: Python's mutable default arguments persist
- **Solution**: Use None and initialize inside function

### 4. **Inefficient String Concatenation**
- **Problem**: Strings are immutable, concatenation is O(n)
- **Solution**: Use list and join at the end

## Testing Strategy

Each solution includes:
1. **Edge cases**: Empty inputs, single elements
2. **Normal cases**: Typical inputs
3. **Boundary cases**: Maximum/minimum values
4. **Special cases**: Duplicates, negative numbers

## How to Run

```bash
# Run all tests
python recursive_solutions.py

# Import specific functions
from recursive_solutions import quicksort, binary_search_recursive

# Use individual functions
result = quicksort([3, 1, 4, 1, 5, 9])
index = binary_search_recursive([1, 2, 3, 4, 5], 3)
```

## Learning Path Recommendations

1. **Start with Basic Level**: Master simple recursion patterns
2. **Practice Tracing**: Manually trace through recursive calls
3. **Visualize Call Stack**: Draw recursion trees
4. **Identify Base Cases**: Always define clear stopping conditions
5. **Think Recursively**: Break problems into smaller similar problems
6. **Optimize Later**: Get working solution first, then optimize

## Advanced Topics to Explore

1. **Dynamic Programming**: Memoization and tabulation
2. **Mutual Recursion**: Functions calling each other
3. **Continuation-Passing Style**: Advanced functional programming
4. **Trampolining**: Technique to avoid stack overflow
5. **Y Combinator**: Implementing recursion without named functions

## Performance Considerations

- **Python Recursion Limit**: Default is ~1000 calls
- **Stack Space**: Each call uses stack memory
- **Tail Call Optimization**: Not supported in Python
- **When to Avoid Recursion**: 
  - Very deep recursion (>1000 levels)
  - Simple iterative solutions available
  - Performance-critical code with large inputs

## Conclusion

Recursive thinking is a powerful problem-solving technique. While not always the most efficient, recursive solutions often provide elegant and intuitive approaches to complex problems. Master these patterns to enhance your problem-solving toolkit!