"""
Tree Operations - Advanced Level

Advanced recursive functions for tree operations.
"""

from data_structures.binary_tree import TreeNode


def max_depth_binary_tree(root):
    """9. Find maximum depth of binary tree recursively
    
    Args:
        root (TreeNode): Root of the binary tree
        
    Returns:
        int: Maximum depth of the tree
        
    Example:
        >>> root = TreeNode(3)
        >>> root.left = TreeNode(9)
        >>> root.right = TreeNode(20)
        >>> root.right.left = TreeNode(15)
        >>> root.right.right = TreeNode(7)
        >>> max_depth_binary_tree(root)
        3
    """
    if root is None:
        return 0
    
    left_depth = max_depth_binary_tree(root.left)
    right_depth = max_depth_binary_tree(root.right)
    
    return 1 + max(left_depth, right_depth)