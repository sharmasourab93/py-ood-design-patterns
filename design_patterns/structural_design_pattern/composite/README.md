# Composite Pattern

The Composite pattern lets you treat a single object and a collection of objects through the same interface.

## Before: Handle Singles And Groups Differently

Source idea from `composite_example.py`.

```python
for m in family:
    if m.birthdate < earliest_date:
        oldest = m

for s in singles:
    if s.birthdate < earliest_date:
        oldest = s
```

## After: Give Both The Same Operation

Source idea from `composite_applied.py`.

```python
class Person(AbsComposite):
    def get_oldest(self):
        return self


class Tree(Iterable, AbsComposite):
    def get_oldest(self):
        def f(t1, t2):
            t1_, t2_ = t1.get_oldest(), t2.get_oldest()
            return t1_ if t1.birthdate < t2_.birthdate else t2_

        return reduce(f, self, NullPerson())
```

## Takeaway

Composite is useful when leaf objects and grouped objects should answer the same kind of request.
