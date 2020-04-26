EMPTY = 0
NOT_EMPTY = 1
AT_CHECKOUT = 2
PAID_FOR = 3


class ShoppingCart:
    def __init__(self):
        self.state = EMPTY
        self._items = 0
        
    def add_item(self):
        if self.state == EMPTY:
            print("You added the first item")
            self.state = NOT_EMPTY
            self._items += 1
            
        elif self.state == NOT_EMPTY:
            self._items += 1
            print("You now have {} items in your cart".format(self._items))
            
        elif self.state == AT_CHECKOUT:
            print("You can't add new items at checkout!")
        else:
            print("You can't add items after payment!.")
            
    def remove_item(self):
        if self.state == EMPTY:
            print("Your cart is empty! Nothing to remove!!")
            
        elif self.state == NOT_EMPTY:
            self._items -= 1
            print("You now have {} items in  your cart.".format(self._items))
            if self._items == 0:
                self.state = EMPTY
                
        elif self.state == AT_CHECKOUT:
            self._items -= 1
            print("You now have {} items in your cart".format(self._items))
            if self._items == 0:
                self.state == EMPTY
            else:
                self.state = NOT_EMPTY
        
        else:
            print("You can't add items after payment!")
            
    def checkout(self):
        if self.state == EMPTY:
            print("Your cart is empty. Go Shopping")
        
        elif self.state == NOT_EMPTY:
            print("You now have {} items in your cart".format(self._items))
            self.state = AT_CHECKOUT
            
        elif self.state == AT_CHECKOUT:
            print("You are already at checkout ")
            
        else:
            print("You can't go back to checkout after payment.")
            
    def paid_for(self):
        
        if self.state == EMPTY:
            print("Your cart is empty. How did you get here?")
        
        elif self.state == NOT_EMPTY:
            print("You must go to checkout for payment")
        
        elif self.state == AT_CHECKOUT:
            print("You paid for {} items".format(self._items))
            self._items = 0
            self.state = EMPTY
            
        else:
            print("You already paid for your purchases.")
            
            
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item()
    cart.remove_item()
    cart.add_item()
    cart.add_item()
    cart.add_item()
    cart.remove_item()
    cart.checkout()
    cart.paid_for()
    cart.add_item()
    cart.checkout()
    cart.paid_for()
