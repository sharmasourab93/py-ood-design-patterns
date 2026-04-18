# Adapter Pattern

The Adapter pattern makes incompatible interfaces work together. It is useful when existing classes already solve the right problem but expose the wrong interface.

## Problem Shape

Source idea from `adapter_example.py`.

```python
class Customer(object):
    @property
    def address(self):
        return self._address


class Vendor(object):
    @property
    def number(self):
        return self._number

    @property
    def street(self):
        return self._street
```

## Object Adapter

Source idea from `object_adapater_pattern_example.py`.

```python
class VendAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return "{} {}".format(self.adaptee.number, self.adaptee.street)
```

## Takeaway

Use Adapter when a class has useful behavior but the interface does not match what the rest of the code expects.
