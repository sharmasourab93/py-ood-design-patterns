# Iterator Pattern

The Iterator pattern gives a standard way to traverse a collection without exposing how the collection is stored internally.

## Basic Direction

Source idea from `iterator_example.py`.

```python
class Employees(object):
    _employees = {}
    _headcount = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def get_employee(self, i):
        return self._employees[i]
```

Usage in the simple version:

```python
for i in range(1, employees.headcount + 1):
    employee = employees.get_employee(i)
    print(employee.empid, employee.name)
```

## Improved Direction: Use Python Iteration Protocol

Source idea from `iterator_collections_example.py`.

```python
class Employees(Iterator):
    def __iter__(self):
        self._empid = 0
        return self

    def __next__(self):
        if self._empid < self._headcount:
            self._empid += 1
            return self._employees[self._empid]
        raise StopIteration
```

An even more Pythonic version appears in `iterator_using_generator_example_applied.py`:

```python
class Employees(Iterable):
    def __iter__(self):
        return (e for e in self._employees.values())
```

## Takeaway

In Python, the Iterator pattern often appears through `__iter__`, `__next__`, and generators rather than a heavy formal pattern implementation.
