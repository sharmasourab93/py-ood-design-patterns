# Abstract Factory: Before Applying The Pattern

This folder shows the branching logic that motivates Abstract Factory. The concrete car classes are simple; the real issue is that the caller is making every creation decision itself.

## Core Example

```python
if maker == "gm":
    if edition == "Econonmy":
        car = ChevySpark()
    elif edition == "Sport":
        car = ChevyCamaro()
    elif edition == "Luxury":
        car = CadillacCTS()
```

## Why This Gets Hard To Maintain

- more makers mean more nested branching
- more editions mean more branching again
- caller code is tightly coupled to every product class
