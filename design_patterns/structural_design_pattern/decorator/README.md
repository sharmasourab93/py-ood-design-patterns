# Decorator Pattern

The Decorator pattern adds behavior to an object dynamically by wrapping it. It avoids creating a large inheritance tree for every possible combination of features.

## Before: Class Explosion

Source idea from `decorator explained.py`.

```python
class Economy4CylWhiteVinyl(Economy):
    @property
    def description(self):
        return "Economy, White, 4 cylinder, vinyl upholstery"


class Economy6CylWhiteVinyl(Economy):
    @property
    def description(self):
        return "Economy, 6 cylinder, White Vinyl, Upholstery"
```

## After: Wrap The Car With Options

Source idea from `decos/abs_decorator.py` and `decos/black.py`.

```python
class AbsDecorator(AbsCar):
    def __init__(self, car):
        self._car = car


class Black(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ", midnight black"

    @property
    def cost(self):
        return self.car.cost + 1800.00
```

Usage from `__main__.py`:

```python
car = Economy()
car = V6(car)
car = Vinyl(car)
car = Black(car)
```

## Takeaway

Use Decorator when features should be combined flexibly at runtime instead of encoded as separate subclasses.
