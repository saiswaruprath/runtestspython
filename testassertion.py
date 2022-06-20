\**using stack, pop, peek, push and assertequal, is_empty etc to do test assertions using pithon*/
from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(5)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(),3)
        self.assertEqual(self.stack.peek(),5)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(5)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(),3)
      

    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())

        
"""Implements a Stack data structure"""
from typing import Any


class Stack:
    """Implements a Stack data structure"""

    def __init__(self):
        """Constructor"""
        self.items = [] 
    
    def push(self, data: Any) -> None: 
        """Places an item onto the stack"""
        self.items.append(data) 
    
    def pop(self) -> Any:
        """Removes an item from the stack and returns it"""
        return self.items.pop() 
        
    def peek(self) -> Any:
        """Returns the item at the top of the stack without removing it"""
        return self.items[-1] 
        
    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise returns False"""
        return len(self.items) == 0        
