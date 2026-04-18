class InventoryService:
    def check_stock(self, sku):
        print(f"Inventory checked for {sku}")
        return True


class PaymentService:
    def charge(self, customer, amount):
        print(f"Charged {customer} ${amount}")
        return True


class ShippingService:
    def ship(self, customer, sku):
        print(f"Shipment created for {customer}: {sku}")


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


if __name__ == "__main__":
    facade = OrderFacade()
    facade.place_order("Alice", "BOOK-101", 29.99)
