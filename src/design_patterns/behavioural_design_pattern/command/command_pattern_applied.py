""""
Re-implement the order processing system
Use Command Pattern
Rebuild the main program to use it
"""

import abc
import sys


class AbsCommand(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass


class AbsOrderCommand(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def description(self):
        pass


class CommandExecutor(object):

    def execute_command(self, args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "UpdateQuantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unrecognized command: " + args[0])

    def create_order(self):
        pass

    def update_quantity(self, val):
        print(val)
        old_val = 5
        print("Database Updated")
        print("Loggin Updated quantity from %s to %s" % (old_val, val))

    def ship_order(self):
        pass


class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = "UpdateQuantity"
    description = name + " number"

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        # Simulate database update
        print("Updated Database")
        # Simulate logging the update
        print("Logging: Updated Quantity from  %s to %s" % (oldqty, self.newqty))


class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]
        pass

    def execute(self):
        print("No Command names %s" % self._command)


class CreateOrder(AbsOrderCommand):
    name = description = "CreateOrder"

    def execute(self):
        raise NotImplementedError


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = description = "ShipOrder"

    def execute(self):
        raise NotImplementedError


def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)

    return dict([cls.name, cls] for cls in commands)


def print_usages(commands):
    print("Usage:" + "python -m Command BeforeCommand [arguments]")
    print("Commands:")
    for command in commands.values():
        print("\t%s" % command.description)


def parse_commands(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


if __name__ == "__main__":
    commands = get_commands()
    if len(sys.argv) < 2:
        print_usages(commands)
        exit()

    commands = parse_commands(commands, sys.argv[1:])
    commands.execute()
