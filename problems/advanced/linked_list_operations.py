"""
Linked List Operations - Advanced Level

Advanced recursive functions for linked list operations.
"""

from data_structures.linked_list import ListNode


def detect_cycle_recursive(head, slow=None, fast=None):
    """2. Detect cycle in linked list recursively
    
    Uses Floyd's Cycle Detection Algorithm (Tortoise and Hare) implemented recursively.
    
    Args:
        head (ListNode): Head of the linked list
        slow (ListNode): Slow pointer (moves one step)
        fast (ListNode): Fast pointer (moves two steps)
        
    Returns:
        bool: True if cycle exists, False otherwise
        
    Example:
        >>> # Create linked list with cycle: 1 -> 2 -> 3 -> 1
        >>> node1 = ListNode(1)
        >>> node2 = ListNode(2) 
        >>> node3 = ListNode(3)
        >>> node1.next = node2
        >>> node2.next = node3
        >>> node3.next = node1  # Creates cycle
        >>> detect_cycle_recursive(node1)
        True
    """
    if head is None:
        return False
    
    if slow is None:
        slow = head
        fast = head
    
    if fast is None or fast.next is None:
        return False
    
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
        return True
    
    return detect_cycle_recursive(head, slow, fast)