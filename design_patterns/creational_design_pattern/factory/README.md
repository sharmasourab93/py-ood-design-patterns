# Factory Pattern

Factory patterns centralize object creation so callers do not need to know every concrete type directly.

## Before: Branch On Concrete Names

Source idea from `factory_explained.py`.

```python
def getcar(carname):
    if carname == "Chevy":
        return ChevyVolt()
    elif carname == "Ford":
        return FordFocus()
    elif carname == "Jeep":
        return JeepSahara()
    else:
        return NullCar(carname)
```

## Applied Direction

Source idea from `factory_applied.py`.

```python
class AutoFactory(object):
    autos = {}

    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname](carname)
        else:
            return self.autos["NullCar"](carname)
```

## Takeaway

Use a factory when callers should ask for an object without carrying the full construction logic themselves.
