# State Pattern

The State pattern lets an object change its behavior when its internal state changes. Instead of storing many condition branches in one class, state-specific behavior is delegated to state objects.

## Before: One Class Controls Every State Branch

Source idea from `state_example.py`.

```python
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
```

## After: Each State Handles Its Own Behavior

Source idea from `state_applied.py`.

```python
class Empty(AbsState):
    def add_item(self):
        self._cart.items += 1
        print("You added the first item")
        self._cart.state = self._cart.not_empty


class NotEmpty(AbsState):
    def checkout(self):
        print("Done shopping. Let's check out!")
        self._cart.state = self._cart.check_out
```

The cart delegates:

```python
class ShoppingCart:
    def add_item(self):
        self.state.add_item()
```

## Takeaway

If behavior changes heavily based on internal state, moving that behavior into state objects usually makes the design easier to understand.
