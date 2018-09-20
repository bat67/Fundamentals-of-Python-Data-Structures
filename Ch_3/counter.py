"""
File: counter.py

Defines a Counter class for counting.
"""

class Counter(object):
    """Models a counter."""
    
    # Class variable
    instances = 0
    
   #Constructor
    def __init__(self):
        """Sets up the counter."""
        Counter.instances += 1
        self.reset()
        
    # Mutator methods
    def reset(self):
        """Sets the counter to 0."""
        self._value = 0
        
    def increment(self, amount = 1):
        """Adds amount to the counter."""
        self._value += amount
        

   def decrement(self, amount = 1):
       """Subtracts amount from the counter."""
       self._value -= amount
        

    # Accessor methods
    def getValue(self):
        """Returns the counter's value."""
        return self._value
    

   def __str__(self):
        """Returns the string representation of the counter."""
        return str(self._value)
    
    def __eq__(self, other):
        """Returns True if self equals other

        or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self._value == other._value
