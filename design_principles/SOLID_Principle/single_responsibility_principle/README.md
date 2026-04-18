# Single Responsibility Principle

The Single Responsibility Principle says a module, class, or function should have one primary reason to change. When many concerns are mixed together, the code becomes harder to test and harder to modify safely.

## Problem Example

Source idea from `single_responsibility_principle.py`.

```python
def create_objects(name, data, send=False, code=None):
    data = [r for r in data if r[0] and r[1]]
    keys = ["{}:{}".format(*r) for r in data]

    existing_objects = dict(
        Object.objects.filter(name=name, key__in=keys).values_list("key", "uid")
    )

    with transaction.commit_on_success():
        for (pid, w, uid), key in izip(data, keys):
            ...
            result = Result.objects.filter(
                Q(barcode=pid) | Q(oid=pid)
            ).latest("created")
            ...
            t = Object.objects.create(
                name=name, w=w, key=key, result=result, uid=uid, name_code=code
            )
            ...
            Client().Update(result)
            ...
            Result.objects.filter(id=result.id).update(...)
```

## What This One Function Is Doing

- filtering input data
- building keys
- querying persistence storage
- creating domain objects
- triggering notifications
- updating result state
- deciding workflow behavior

## Why This Violates SRP

The function has more than one reason to change:

- business rules may change
- persistence logic may change
- notification logic may change
- status update rules may change

## Repository Note

`single_responsibility_principle_applied.py` is currently empty, so the repository only contains the overloaded version of this example.

## Takeaway

If one function handles validation, storage, business rules, and side effects together, it is carrying too many responsibilities.
