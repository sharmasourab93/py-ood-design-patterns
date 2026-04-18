# Abstract Factory: Applied Version

This folder contains the structured implementation of Abstract Factory. The caller now works with factory types instead of branching on every product choice.

## Main Usage

From `__main__.py`:

```python
for factory in FordFactory, GMFactory:
    car = factory.create_economy()
    car.start()
    car.stop()
```

## What This Separates

- factory classes decide which products belong to a family
- product classes only implement product behavior
- caller code asks for a category, not a concrete class name
