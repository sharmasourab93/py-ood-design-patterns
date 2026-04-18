# Applied Factories

The factory side of the pattern is responsible for creating matching product families.

## Factory Contract

From `abs_factory.py`:

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

## Concrete Factory Example

From `ford_factory.py`:

```python
class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()
```

## Takeaway

Switching the factory switches the whole product family.
