# Command Pattern

The Command pattern turns a request into an object. This separates the code that asks for an action from the code that actually performs it.

## Before: One Executor Handles Every Command

Source idea from `command_pattern_example.py`.

```python
class CommandExecutor(object):
    def execute_command(self, args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "update_quantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unrecognized command: " + args[0])
```

## After: Represent Each Command As An Object

Source idea from `command_pattern_applied.py`.

```python
class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = "UpdateQuantity"
    description = name + " number"

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        print("Updated Database")
        print("Logging: Updated Quantity from  %s to %s" % (oldqty, self.newqty))
```

The command lookup becomes separate:

```python
def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([cls.name, cls] for cls in commands)
```

## Takeaway

Use Command when you want actions to be first-class objects that can be selected, queued, logged, or extended independently.
