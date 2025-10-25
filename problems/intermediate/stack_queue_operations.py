"""
Stack and Queue Operations - Intermediate Level

Data structures and their recursive operations.
"""


class StackUsingQueues:
    """10. Stack using two queues with recursive operations
    
    A stack implementation using two queues where stack operations
    are implemented recursively.
    
    Example:
        >>> stack = StackUsingQueues()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.top()
        1
    """
    
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def push(self, x):
        """Push element onto stack"""
        self.q1.append(x)
    
    def _move_elements(self, source, dest, keep_last=False):
        """Recursively move elements between queues
        
        Args:
            source (list): Source queue
            dest (list): Destination queue
            keep_last (bool): Whether to keep the last element in source
        """
        if len(source) == (1 if keep_last else 0):
            return
        dest.append(source.pop(0))
        self._move_elements(source, dest, keep_last)
    
    def pop(self):
        """Pop element from stack (LIFO)
        
        Returns:
            Element from top of stack or None if empty
        """
        if not self.q1:
            return None
        
        # Move all but last element to q2
        self._move_elements(self.q1, self.q2, keep_last=True)
        
        # Pop the last element
        result = self.q1.pop(0)
        
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        
        return result
    
    def top(self):
        """Get top element without removing it
        
        Returns:
            Top element or None if empty
        """
        if not self.q1:
            return None
        
        self._move_elements(self.q1, self.q2, keep_last=True)
        result = self.q1[0]
        self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        
        return result