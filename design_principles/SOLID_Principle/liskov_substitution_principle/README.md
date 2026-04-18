# Liskov Substitution Principle

The Liskov Substitution Principle says a subtype should be usable anywhere its parent type is expected, without breaking the logic of the program.

## Example

Source idea from `liskov_substitution_principle.py`.

```python
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
```

## What This Example Is Showing

The file is intentionally minimal. The main teaching point is that child classes should preserve the expectations created by the parent class.

When reading any hierarchy, ask:

- Can the child be used wherever the parent is expected?
- Does the child require extra assumptions?
- Does the child break any behavior the caller relies on?

## Supporting Material

- `liskovsp.jpg` provides an additional visual reference.

## Takeaway

Inheritance is not only about code reuse. It is also a behavioral promise.
