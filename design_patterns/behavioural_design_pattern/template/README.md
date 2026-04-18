# Template Method Pattern

The Template Method pattern defines the skeleton of an algorithm in a base class and lets subclasses customize individual steps.

## Before: Repeated Workflow Structure

Source idea from `template_pattern_example.py`.

```python
class Bus(object):
    def bus_trip(self):
        self.start_diesel()
        self.leave_terminal()
        self.drive_to_destination()
        self.arrive_at_destination()


class Airplane(object):
    def plane_trip(self):
        self.start_gas_turbines()
        self.leave_terminal()
        self.fly_to_destination()
        self.land_at_destination()
```

## After: Base Class Owns The Common Sequence

Source idea from `template_pattern_applied.py`.

```python
class AbsTransport(metaclass=abc.ABCMeta):
    def take_trip(self):
        self.start_engine()
        self.leave_terminal()
        self.entertainment()
        self.travel_to_destination()
        self.arrive_at_destination()
```

A concrete subclass only fills in the varying steps:

```python
class Bus(AbsTransport):
    def start_engine(self):
        print("Starting the Cummins Diesel engine")

    def travel_to_destination(self):
        print("Driving")
```

## Takeaway

Use Template Method when several classes follow the same algorithm shape but differ in a few steps.
