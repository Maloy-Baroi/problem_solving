"""
Test Suite for Basic Level Problems

Tests for all basic level recursive functions.
"""

from problems.basic import (
    reverse_string, is_palindrome_number, find_largest, count_vowels,
    factorial_recursive, factorial_iterative_as_recursive, remove_duplicates,
    are_anagrams, fibonacci_sequence, find_second_largest, has_unique_chars
)


def test_basic_functions():
    """Test all basic level functions"""
    print("=" * 50)
    print("TESTING BASIC LEVEL FUNCTIONS")
    print("=" * 50)
    
    # 1. Reverse string
    print("1. Reverse string:", reverse_string("hello"))
    
    # 2. Palindrome number
    print("2. Is 12321 palindrome?", is_palindrome_number(12321))
    print("   Is 12345 palindrome?", is_palindrome_number(12345))
    
    # 3. Largest element
    print("3. Largest in [3,7,2,9,1]:", find_largest([3, 7, 2, 9, 1]))
    
    # 4. Count vowels
    print("4. Vowels in 'Hello World':", count_vowels("Hello World"))
    
    # 5. Factorial
    print("5a. Factorial of 5 (recursive):", factorial_recursive(5))
    print("5b. Factorial of 5 (tail recursive):", factorial_iterative_as_recursive(5))
    
    # 6. Remove duplicates
    print("6. Remove duplicates from [1,2,2,3,4,4,5]:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    
    # 7. Anagrams
    print("7. Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))
    
    # 8. Fibonacci
    print("8. First 8 Fibonacci numbers:", fibonacci_sequence(8))
    
    # 9. Second largest
    print("9. Second largest in [10, 20, 30, 40, 30]:", find_second_largest([10, 20, 30, 40, 30]))
    
    # 10. Unique characters
    print("10. Does 'abcdef' have unique chars?", has_unique_chars("abcdef"))
    print("    Does 'hello' have unique chars?", has_unique_chars("hello"))