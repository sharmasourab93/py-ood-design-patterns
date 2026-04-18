# Abstract Factory Pattern

Abstract Factory creates families of related objects through a common factory interface. The caller asks for a product family, not for a specific class.

## Problem Shape

Source idea from `example/__main__.py`.

```python
if maker == "gm":
    if edition == "Econonmy":
        car = ChevySpark()
    elif edition == "Sport":
        car = ChevyCamaro()
    elif edition == "Luxury":
        car = CadillacCTS()
elif maker == "ford":
    if edition == "Econonmy":
        car = FordFiesta()
    elif edition == "Sport":
        car = FordMustang()
    elif edition == "Luxury":
        car = LincolnMKS()
```

## Applied Direction

Source idea from `applied/factories/abs_factory.py`.

```python
class AbsFactory(abc.ABC):
    @abc.abstractstaticmethod
    def create_economy():
        pass

    @abc.abstractstaticmethod
    def create_sport():
        pass

    @abc.abstractstaticmethod
    def create_luxury():
        pass
```

Concrete factory:

```python
class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()
```

## Takeaway

Use Abstract Factory when products come in families and the caller should stay independent of concrete product classes.
