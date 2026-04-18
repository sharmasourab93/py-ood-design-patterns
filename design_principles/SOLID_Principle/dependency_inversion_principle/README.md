# Dependency Inversion Principle

The Dependency Inversion Principle says high-level modules should depend on abstractions instead of depending directly on low-level concrete classes.

## Before: High-Level Code Depends On Concrete Types

Source idea from `dependency_inversion_principle.py`.

```python
class Manager(object):
    def __init__(self):
        self.developers = []
        self.designers = []
        self.testers = []

    def add_developer(self, dev):
        self.developers.append(dev)

    def add_designers(self, design):
        self.designers.append(design)

    def add_testers(self, testers):
        self.testers.append(testers)
```

## After: Depend On A Shared Abstraction

Source idea from `dependency_inversion_principle_corrected.py`.

```python
class Employee(object):
    def work(self):
        pass


class Manager:
    def __init__(self):
        self.employees = []

    def add_employee(self, a):
        self.employees.append(a)
```

Concrete types now depend on the abstraction:

```python
class Developer(Employee):
    def work(self):
        print("turning coffee into code")


class Designer(Employee):
    def work(self):
        print("turning lines to wireframes")
```

## Takeaway

When a high-level object depends on an abstraction, new concrete implementations can be introduced with less change to the surrounding code.
