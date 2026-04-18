# Facade Pattern

The Facade pattern provides a simpler interface to a more complex subsystem. It is useful when the caller should interact with one clean entry point instead of coordinating multiple service objects manually.

## Example

Source idea from `facade_example.py`.

```python
class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payment = PaymentService()
        self.shipping = ShippingService()

    def place_order(self, customer, sku, amount):
        if not self.inventory.check_stock(sku):
            print("Out of stock")
            return
        if not self.payment.charge(customer, amount):
            print("Payment failed")
            return
        self.shipping.ship(customer, sku)
        print("Order completed")
```

Usage:

```python
facade = OrderFacade()
facade.place_order("Alice", "BOOK-101", 29.99)
```

Output:

```text
Inventory checked for BOOK-101
Charged Alice $29.99
Shipment created for Alice: BOOK-101
Order completed
```

## Takeaway

Use Facade when callers should not need to understand or coordinate an entire subsystem on their own.
