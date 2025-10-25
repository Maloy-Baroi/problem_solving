"""
Test Suite for Problem Solving Library

This module contains all test functions organized by difficulty level.
"""

from .test_basic import test_basic_functions
from .test_intermediate import test_intermediate_functions  
from .test_advanced import test_advanced_functions

__all__ = [
    'test_basic_functions',
    'test_intermediate_functions',
    'test_advanced_functions'
]


def run_all_tests():
    """Run all test suites"""
    print("Running all test suites...\n")
    test_basic_functions()
    test_intermediate_functions()
    test_advanced_functions()
    print("\nAll tests completed!")