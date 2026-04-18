# Singleton Pattern

Singleton restricts a class so only one shared instance exists. This repository shows multiple ways to implement it, along with the common trade-offs.

## Classic Singleton Style

Source idea from `logger_classic.py`.

```python
class Logger(object):
    @staticmethod
    def instance():
        if "_instance" not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance
```

## Base-Class Singleton

Source idea from `singleton_applied.py`.

```python
class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
```

## Metaclass Version

Source idea from `singleton_meta.py`.

```python
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]
```

## Important Design Note

The code comments in this folder correctly point out the common drawbacks:

- hidden global state
- harder testing
- tighter coupling

## Takeaway

Singleton is useful to understand, but it should be used carefully because convenience often comes with design cost.
