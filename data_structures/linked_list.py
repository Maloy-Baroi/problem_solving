"""
Linked List Data Structure

Node class for linked list operations.
"""


class ListNode:
    """Node class for linked list operations
    
    Attributes:
        val: Value stored in the node
        next: Reference to the next node
        
    Example:
        >>> node1 = ListNode(1)
        >>> node2 = ListNode(2)
        >>> node1.next = node2
        >>> print(node1.val)  # 1
        >>> print(node1.next.val)  # 2
    """
    
    def __init__(self, val=0, next=None):
        """Initialize a new ListNode
        
        Args:
            val: Value for the node (default: 0)
            next (ListNode): Reference to next node (default: None)
        """
        self.val = val
        self.next = next
    
    def __str__(self):
        """String representation of the node"""
        return f"ListNode(val={self.val})"
    
    def __repr__(self):
        """Detailed representation of the node"""
        return f"ListNode(val={self.val}, next={self.next is not None})"