from abc import ABC, abstractmethod

"""
Variations
strategies as function
strategies as lambdas

Fixed the problems we discovered
test algorithms in isolation
Test the outer code with mock algorithms
No more if/elif/else
"""


# Dependency Inversion Patter strategy
class Order:
    def __init__(self):
        #self._shipper = shipper
        pass


class AbsStrategy(ABC):
    
    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
        pass
        

class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3

    
class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 4
    

class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 5


class ShippingCost:
    def __init__(self, strategy):
        self._strategy = strategy
        
    def shipping_cost(self, order):
        return self._strategy.calculate(order)
    

if __name__ == '__main__':
    # Test Federal Express Shipping
    order = Order()
    strategy = FedExStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 3.0
    
    # Test UPS Shipping

    order = Order()
    strategy = UPSStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 5.0
    
    # Test Postal Service Shipping

    order = Order()
    strategy = PostalStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 4.0
    
    print("Tests Passed.")
