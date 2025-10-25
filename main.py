#!/usr/bin/env python3
"""
Recursive Solutions for Programming Problems - Main Entry Point

A comprehensive library of recursive solutions organized by difficulty level.
This is the main entry point that demonstrates all implemented algorithms.

Usage:
    python main.py              # Run all tests
    python main.py --basic      # Run basic tests only
    python main.py --inter      # Run intermediate tests only
    python main.py --advanced   # Run advanced tests only
"""

import sys
import argparse
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from tests import run_all_tests, test_basic_functions, test_intermediate_functions, test_advanced_functions


def main():
    """Main entry point for the problem solving library"""
    parser = argparse.ArgumentParser(
        description="Recursive Problem Solving Library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                 # Run all tests
  python main.py --basic         # Run basic level tests only
  python main.py --intermediate  # Run intermediate level tests only
  python main.py --advanced      # Run advanced level tests only
        """
    )
    
    parser.add_argument(
        '--basic', '-b',
        action='store_true',
        help='Run basic level tests only'
    )
    
    parser.add_argument(
        '--intermediate', '--inter', '-i',
        action='store_true',
        help='Run intermediate level tests only'
    )
    
    parser.add_argument(
        '--advanced', '-a',
        action='store_true',
        help='Run advanced level tests only'
    )
    
    args = parser.parse_args()
    
    print("🚀 Recursive Problem Solving Library")
    print("=" * 60)
    print("A comprehensive collection of recursive solutions")
    print("organized by difficulty level: Basic, Intermediate, Advanced")
    print("=" * 60)
    
    try:
        if args.basic:
            test_basic_functions()
        elif args.intermediate:
            test_intermediate_functions() 
        elif args.advanced:
            test_advanced_functions()
        else:
            # Run all tests if no specific level is chosen
            run_all_tests()
            
        print("\n" + "=" * 60)
        print("✅ Execution completed successfully!")
        print("=" * 60)
            
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()