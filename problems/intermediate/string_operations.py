"""
String Operations - Intermediate Level

Recursive functions for intermediate-level string operations.
"""


def first_non_repeating(s, index=0, char_count=None):
    """2. Find first non-repeating character recursively
    
    Args:
        s (str): Input string
        index (int): Current index (default: 0)
        char_count (dict): Character frequency count (default: None)
        
    Returns:
        str/None: First non-repeating character or None if not found
        
    Example:
        >>> first_non_repeating("leetcode")
        'l'
    """
    if char_count is None:
        # First pass: count all characters
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
    
    if index >= len(s):
        return None
    
    if char_count[s[index]] == 1:
        return s[index]
    
    return first_non_repeating(s, index + 1, char_count)


def one_edit_away(s1, s2, i=0, j=0, edit_used=False):
    """8. Check if two strings are one edit away recursively
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        i (int): Index for first string (default: 0)
        j (int): Index for second string (default: 0)
        edit_used (bool): Whether an edit has been used (default: False)
        
    Returns:
        bool: True if strings are one edit away, False otherwise
        
    Example:
        >>> one_edit_away("pale", "ple")
        True
    """
    if i >= len(s1):
        return j >= len(s2) - 1 if not edit_used else j >= len(s2)
    if j >= len(s2):
        return i >= len(s1) - 1 if not edit_used else i >= len(s1)
    
    if s1[i] == s2[j]:
        return one_edit_away(s1, s2, i + 1, j + 1, edit_used)
    
    if edit_used:
        return False
    
    # Try insert
    insert = one_edit_away(s1, s2, i, j + 1, True)
    # Try delete
    delete = one_edit_away(s1, s2, i + 1, j, True)
    # Try replace
    replace = one_edit_away(s1, s2, i + 1, j + 1, True)
    
    return insert or delete or replace


def string_compression(s, index=0, result="", count=1):
    """9. Compress string recursively
    
    Args:
        s (str): Input string
        index (int): Current index (default: 0)
        result (str): Result string (default: "")
        count (int): Current character count (default: 1)
        
    Returns:
        str: Compressed string
        
    Example:
        >>> string_compression("aaabbbc")
        'a3b3c1'
    """
    if index >= len(s):
        return result
    
    if index == len(s) - 1:
        return result + s[index] + str(count)
    
    if s[index] == s[index + 1]:
        return string_compression(s, index + 1, result, count + 1)
    else:
        return string_compression(s, index + 1, result + s[index] + str(count), 1)