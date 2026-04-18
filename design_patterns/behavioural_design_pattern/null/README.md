# Null Object Pattern

The Null Object pattern replaces `None` with an object that follows the same interface as the real object. This reduces repetitive null checks in calling code.

## Before: Return `None`

Source idea from `null_pattern_example.py`.

```python
class MyObjectFactory:
    @staticmethod
    def create_object(value):
        if value == "myclass":
            return MyClass()
        else:
            return None
```

## After: Return A Null Implementation

Source idea from `null_pattern_applied.py`.

```python
class NullClass(AbsClass):
    def do_something(self, value):
        print("Not Doing %s." % value)


class MyObjectFactory:
    @staticmethod
    def create_object(value):
        if value == "myclass":
            return MyClass()
        else:
            return NullClass()
```

Usage:

```python
my_obj = MyObjectFactory.create_object("myotherclass")
my_obj.do_something("something")
```

Output:

```text
Not Doing something.
```

## Takeaway

Use Null Object when the caller should keep using a consistent interface even when there is no real object to return.
