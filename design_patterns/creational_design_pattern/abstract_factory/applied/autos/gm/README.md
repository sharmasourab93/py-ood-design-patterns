# GM Product Family

This folder contains GM-side concrete products for the Abstract Factory example.

## Example

From `camaro.py`:

```python
class ChevyCamaro(AbsAuto):
    def start(self):
        print("Chevy Camaro V8 sounding awesome!")

    def stop(self):
        print("Chevy Camaro shutting down.")
```

## Models Represented

- `spark.py`: economy
- `camaro.py`: sport
- `cadillac.py`: luxury
