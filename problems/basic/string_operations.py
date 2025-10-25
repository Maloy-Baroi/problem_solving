"""
String Operations - Basic Level

Recursive functions for basic string manipulation operations.
"""


def reverse_string(s):
    """1. Reverse a string recursively
    
    Args:
        s (str): Input string to reverse
        
    Returns:
        str: Reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def count_vowels(s, index=0):
    """4. Count vowels in a string recursively
    
    Args:
        s (str): Input string
        index (int): Current index (default: 0)
        
    Returns:
        int: Number of vowels in the string
        
    Example:
        >>> count_vowels("Hello World")
        3
    """
    if index >= len(s):
        return 0
    
    vowels = 'aeiouAEIOU'
    count = 1 if s[index] in vowels else 0
    return count + count_vowels(s, index + 1)


def are_anagrams(s1, s2):
    """7. Check if two strings are anagrams recursively
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
        
    Example:
        >>> are_anagrams("listen", "silent")
        True
    """
    if len(s1) != len(s2):
        return False
    
    if len(s1) == 0:
        return True
    
    if s1[0] in s2:
        # Remove first occurrence of s1[0] from s2
        idx = s2.index(s1[0])
        new_s2 = s2[:idx] + s2[idx+1:]
        return are_anagrams(s1[1:], new_s2)
    
    return False


def has_unique_chars(s, index=0, seen=None):
    """10. Check if string has all unique characters recursively
    
    Args:
        s (str): Input string
        index (int): Current index (default: 0)
        seen (set): Set of seen characters (default: None)
        
    Returns:
        bool: True if all characters are unique, False otherwise
        
    Example:
        >>> has_unique_chars("abcdef")
        True
        >>> has_unique_chars("hello")
        False
    """
    if seen is None:
        seen = set()
    
    if index >= len(s):
        return True
    
    if s[index] in seen:
        return False
    
    seen.add(s[index])
    return has_unique_chars(s, index + 1, seen)