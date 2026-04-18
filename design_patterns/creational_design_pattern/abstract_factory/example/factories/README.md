# Example Product Classes

This folder contains the concrete car classes used by the pre-pattern example.

## Example

From `ford.py`:

```python
class FordMustang:
    def start(self):
        print("Ford Mustang roaring and ready to go.")

    def stop(self):
        print("Ford Mustang shutting down.")
```

From `gm.py`:

```python
class ChevySpark:
    def start(self):
        print("Chevy Spark running efficiently.")
```

## Why These Files Matter

These classes are straightforward. The design problem is not inside the products; it is in how the caller chooses between them.
