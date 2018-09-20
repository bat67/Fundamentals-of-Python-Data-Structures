"""
File: customer.py
Author: Ken Lambert

Customer's processing time varies around the average,
so give it a random time between 1 and average time * 2 + 1.

"""

import random

class Customer(object):
    """Represents a customer."""

    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival,
                         arrivalTime,
                         averageTimePerCustomer):
        """Returns a Customer object if the probability 
        of arrival is greater than or equal to a random number.
        Otherwise, returns None, indicating no new customer.
        """                                     
        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None
       
    def __init__(self, arrivalTime, serviceNeeded):
        """Maintains the arrival time and amount of service needed."""
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded

    def arrivalTime(self):
        """Returns the arrival time."""
        return self._arrivalTime
   
    def amountOfServiceNeeded(self):
        """Returns the amount of service needed."""
        return self._amountOfServiceNeeded
   
    def serve(self):
        """Accepts a unit of service from the cashier."""
        self._amountOfServiceNeeded -= 1
