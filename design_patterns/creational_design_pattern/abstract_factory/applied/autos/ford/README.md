# Ford Product Family

This folder contains Ford-side concrete products for the Abstract Factory example.

## Example

From `mustang.py`:

```python
class FordMustang(AbsAuto):
    def start(self):
        print("Ford Mustang roaring and ready to go!")

    def stop(self):
        print("Ford Mustang shutting down.")
```

## Models Represented

- `fiesta.py`: economy
- `mustang.py`: sport
- `lincoln.py`: luxury
