import abc


class AbsState(abc.ABC):
    def __init__(self, context):
        self._cart = context

    @abc.abstractmethod
    def add_item(self):
        pass

    @abc.abstractmethod
    def remove_item(self):
        pass

    @abc.abstractmethod
    def checkout(self):
        pass

    @abc.abstractmethod
    def pay(self):
        pass

    def empty_cart(self):
        pass


class AtCheckOut(AbsState):

    def add_item(self):
        print("You can't add items at the check out counter.")

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print("You now have %s items in your cart." % self._cart.items)
        else:
            print("Your cart is empty again.")
            self._cart.state = self._cart.empty

    def checkout(self):
        print("You're already at checkout.")

    def pay(self):
        print("You paid for %s items." % self._cart.items)
        self._cart.state = self._cart.paid_for

    def empty_cart(self):
        self._cart.items = 0
        self._cart.state = self._cart.empty
        print("Your cart is empty again.")


class Empty(AbsState):

    def add_item(self):
        self._cart.items += 1
        print("You added the first item")
        self._cart.state = self._cart.not_empty

    def remove_item(self):
        print("Your cart is empty! Nothing to remove!!")

    def checkout(self):
        print("Your cart is empty. Go shopping!")

    def pay(self):
        print("Your cart is empty. How did you get here?")

    def empty_cart(self):
        print("Your cart is already empty.")


class NotEmpty(AbsState):

    def add_item(self):
        self._cart.items += 1
        print("You now have %s items in your cart." % self._cart.items)

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print("You now have %s items in your cart." % self._cart.items)
        else:
            print("Your cart is empty again.")
            self._cart.state = self._cart.empty

    def checkout(self):
        print("Done shopping. Let's check out!")
        self._cart.state = self._cart.check_out

    def pay(self):
        print("You have to go to checkout to pay!")

    def empty_cart(self):
        print("Your can only empty the cart at checkout.")


class PaidFor(AbsState):

    def add_item(self):
        print(
            "You already paid for your purchases. Want to shop some more? Get a new shopping cart!"
        )

    def remove_item(self):
        print("You already paid for your purchases and can't remove any.")

    def checkout(self):
        print("Why are you back here?  You already paid!")

    def pay(self):
        print("You already paid.  You can't pay twice!")

    def empty_cart(self):
        print("You paid already. Time to go home!")


class ShoppingCart:
    def __init__(self):
        self.empty = Empty(self)
        self.not_empty = NotEmpty(self)
        self.check_out = AtCheckOut(self)
        self.paid_for = PaidFor(self)

        self.items = 0
        self.state = self.empty

    def add_item(self):
        self.state.add_item()

    def remove_item(self):
        self.state.remove_item()

    def checkout(self):
        self.state.checkout()

    def pay(self):
        self.state.pay()

    def empty_cart(self):
        self.state.empty_cart()


def main():

    print("====> first cart")
    cart = ShoppingCart()
    cart.add_item()
    cart.remove_item()
    cart.add_item()
    cart.add_item()
    cart.add_item()
    cart.remove_item()
    cart.checkout()
    cart.pay()

    # Go shopping again
    print("====> second cart")
    cart = ShoppingCart()
    cart.add_item()
    cart.add_item()
    cart.checkout()
    cart.empty_cart()
    cart.add_item()
    cart.checkout()
    cart.pay()

    # Try to add another item
    print("====> Expect an error here.")
    cart.add_item()


if __name__ == "__main__":
    main()
