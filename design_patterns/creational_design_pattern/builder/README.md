# Builder Pattern

The Builder pattern separates object construction from the final object representation. It is useful when an object has many parts or when the build process should be reusable.

## Before: Large Constructor

Source idea from `builder_example.py`.

```python
computer = Computer(
    case="CoolerMaster N300",
    mainboard="MSI 970",
    cpu="Intel COre i7-4770",
    memory="Corsair Vengeance 16Gb",
    hard_drive="Seagate 2TB",
    video_card="GeForce GTX 1070",
)
```

## After: Build In Steps

Source idea from `builder_applied.py`.

```python
class Director(object):
    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()
```

Concrete builder example:

```python
class MyComputerBuilder(AbsBuilder):
    def get_case(self):
        self._computer.case = "CoolerMaster N300"
```

## Takeaway

Use Builder when construction has multiple steps or when you want different configurations built through the same overall process.
