# Decorator Components

This folder contains the concrete wrappers used by the final Decorator example.

## Shared Wrapper Contract

From `abs_decorator.py`:

```python
class AbsDecorator(AbsCar):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self._car
```

## Concrete Decorator Example

From `vinyl.py`:

```python
class Vinyl(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ", vinyl upholstery"

    @property
    def cost(self):
        return self.car.cost + 500.00
```

## Important Note

Some decorator files contain naming inconsistencies, but the structural idea is still clear: each decorator wraps a car and adds to description and cost.
