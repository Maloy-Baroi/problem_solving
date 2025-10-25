"""
String Operations - Advanced Level

Advanced recursive functions for complex string operations.
"""


def longest_substring_no_repeat(s, start=0, end=0, char_set=None, max_length=0):
    """1. Find longest substring without repeating characters recursively
    
    Args:
        s (str): Input string
        start (int): Start index of current window (default: 0)
        end (int): End index of current window (default: 0)
        char_set (set): Set of characters in current window (default: None)
        max_length (int): Current maximum length found (default: 0)
        
    Returns:
        int: Length of longest substring without repeating characters
        
    Example:
        >>> longest_substring_no_repeat("abcabcbb")
        3
    """
    if char_set is None:
        char_set = set()
    
    if end >= len(s):
        return max_length
    
    if s[end] not in char_set:
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)
        return longest_substring_no_repeat(s, start, end + 1, char_set, max_length)
    else:
        char_set.remove(s[start])
        return longest_substring_no_repeat(s, start + 1, end, char_set, max_length)