# Applied Products

This folder contains the car product abstraction and the concrete brand-specific product families used by the factories.

## Product Contract

From `abs_auto.py`:

```python
class AbsAuto(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
```

## Family Folders

- [ford](ford/README.md)
- [gm](gm/README.md)

## Takeaway

Abstract Factory works by pairing factory families with product families under a shared contract.
