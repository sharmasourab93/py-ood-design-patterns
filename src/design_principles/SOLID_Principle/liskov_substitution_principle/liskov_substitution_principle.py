"""
SOLID Principles: Open Close Principle
LSP definition states that,If S is a subtype of T,
then objects of type T in a program may be replaced
with objects of type S without altering any
of the desirable properties of that program.

1. Preconditions cannot be strengthened in a subtype
2. Postconditions cannot be weakened in a subtype.
3. Invariants of the supertype must be preserved in a subtype.

https://stackoverflow.com/questions/55477952/need-clarity-in-understanding-liskov-substitution-principle
"""


class Switch:
    def __init__(self, ip, dc):
        self.ip = ip
        self.dc = dc


class CiscoSwitch(Switch):
    def __init__(self, ip, dc, zone):
        super().__init__(ip, dc)
        self.zone = zone


class JuniperSwitch(Switch):

    def __init__(self, ip, dc, zone):
        super().__init__(ip, dc)
        self.zone = zone
