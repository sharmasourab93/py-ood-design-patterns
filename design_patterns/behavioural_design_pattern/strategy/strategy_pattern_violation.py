"""
Violates SRP
Violates Open/Clsed Principle
Violates DIP
Log list of if/elif clauses

Done better with Strategy
"""


class Order(object):
    def __init__(self, shipper):
        self._shipper = shipper
    
    @property
    def shipper(self):
        return self._shipper


class Shipper(object):
    fedex = 1
    ups = 2
    postal = 3
    
    def __init__(self):
        pass


class ShippingCost(object):
    # Violates Open Close Principle
    # Usage of too many if else a red flag
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError('Invalid Shipper %s', order.shipper)
    
    def _fedex_cost(self, order):
        return 3.00
    
    def _ups_cost(self, order):
        return 4.00
    
    def _postal_cost(self, order):
        return 5.00


if __name__ == '__main__':
    # Test Federal Express Shipping
    order = Order(Shipper.fedex)
    cost_calculator = ShippingCost() # Violates D in SOLID
    cost = cost_calculator.shipping_cost(order)
    assert cost == 3.0
    
    # Test UPS Shipping
    order = Order(Shipper.ups)
    cost_calculator = ShippingCost()
    cost = cost_calculator.shipping_cost(order)
    assert cost == 4.0
    
    # Test Postal Service Shipping
    order = Order(Shipper.postal)
    cost_calculator = ShippingCost()
    cost = cost_calculator.shipping_cost(order)
    assert cost == 5.0
    
    print("Tests Passed.")
