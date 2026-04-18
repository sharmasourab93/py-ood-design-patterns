# Mediator Pattern

The Mediator pattern centralizes communication between related objects. Instead of objects talking to each other directly, they send messages through a mediator.

## Example

Source idea from `mediator_example.py`.

```python
class ChatMediator:
    def broadcast(self, sender, message):
        for user in self._users:
            if user is not sender:
                user.receive(sender.name, message)
```

Objects communicate through the mediator:

```python
class User:
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self._mediator.broadcast(self, message)
```

Output:

```text
Alice sends: Build is green.
Bob receives from Alice: Build is green.
Charlie receives from Alice: Build is green.
```

## Takeaway

Use Mediator when many peer objects would otherwise become tightly coupled through direct communication.
