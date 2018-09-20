"""
File: cashier.py
Author: Ken Lambert
"""

from linkedqueue import LinkedQueue

class Cashier(object):
    """Represents a cashier."""

    def __init__(self):
        """Maintains a queue of customers,
        number of customers served, total customer wait time,
        and a current customer being processed."""
        self._totalCustomerWaitTime = 0
        self._customersServed = 0
        self._currentCustomer = None
        self._queue = LinkedQueue()

    def addCustomer(self, c):
        """Adds an arriving customer to my line."""
        self._queue.add(c)
   
    def serveCustomers(self, currentTime):
        """Serves my cuatomers during a given unit of time."""
        if self._currentCustomer is None:
            # No customers yet
            if self._queue.isEmpty():
                return
            else:
                # Pop first waiting customer and tally results
                self._currentCustomer = self._queue.pop()
                self._totalCustomerWaitTime += \
                                            currentTime - \
                                            self._currentCustomer.arrivalTime()
                self._customersServed += 1

        # Give a unit of service
        self._currentCustomer.serve()

        # If current customer is finished, send it away   
        if self._currentCustomer.amountOfServiceNeeded() == 0:
            self._currentCustomer = None
   
    def __str__(self):
        """Returns my results: my total customers served,
        my average wait time per customer, and customers left on my queue."""
        result = "TOTALS FOR THE CASHIER\n" + \
                 "Number of customers served:        " + \
                 str(self._customersServed) + "\n"
        if self._customersServed != 0:
            aveWaitTime = self._totalCustomerWaitTime /\
                          self._customersServed
            result += "Number of customers left in queue: " + \
                      str(len(self._queue)) + "\n" + \
                      "Average time customers spend\n" + \
                      "waiting to be served:              " + \
                      "%5.2f" % aveWaitTime
        return result
