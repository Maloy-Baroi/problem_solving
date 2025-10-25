"""
Recursive Problem Solving Library

A comprehensive library of recursive solutions for programming problems,
organized by difficulty level and problem type.

Modules:
    - problems.basic: Basic level recursive problems
    - problems.intermediate: Intermediate level recursive problems  
    - problems.advanced: Advanced level recursive problems
    - data_structures: Common data structures (ListNode, TreeNode)
    - algorithms: Sorting and other algorithms
    - tests: Test suites for all modules
    
Usage:
    from problems.basic import reverse_string, factorial_recursive
    from problems.advanced import longest_substring_no_repeat
    from data_structures import ListNode, TreeNode
    from algorithms import quicksort, mergesort
"""

__version__ = "1.0.0"
__author__ = "Problem Solving Library"
__description__ = "Comprehensive recursive solutions for programming problems"

# Import main modules for easy access
from . import problems
from . import data_structures  
from . import algorithms
from . import tests

__all__ = [
    'problems',
    'data_structures',
    'algorithms', 
    'tests'
]