"""
Binary Tree Data Structure

Node class for binary tree operations.
"""


class TreeNode:
    """Node class for binary tree operations
    
    Attributes:
        val: Value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
        
    Example:
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> print(root.val)  # 1
        >>> print(root.left.val)  # 2
        >>> print(root.right.val)  # 3
    """
    
    def __init__(self, val=0, left=None, right=None):
        """Initialize a new TreeNode
        
        Args:
            val: Value for the node (default: 0)
            left (TreeNode): Reference to left child (default: None)
            right (TreeNode): Reference to right child (default: None)
        """
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        """String representation of the node"""
        return f"TreeNode(val={self.val})"
    
    def __repr__(self):
        """Detailed representation of the node"""
        return f"TreeNode(val={self.val}, left={self.left is not None}, right={self.right is not None})"