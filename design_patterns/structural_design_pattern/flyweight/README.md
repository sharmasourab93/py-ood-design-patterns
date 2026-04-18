# Flyweight Pattern

The Flyweight pattern shares intrinsic state between many objects to reduce memory usage. It is useful when a system creates a large number of similar objects.

## Example

Source idea from `flyweight_example.py`.

```python
factory = TreeFactory()
oak_type = factory.get_tree_type("Oak", "Green")
pine_type = factory.get_tree_type("Pine", "Dark Green")
```

Each tree keeps only its unique position, while the shared species data lives in the flyweight object.

## Takeaway

Use Flyweight when many objects share the same internal data and only a small amount of external state differs.
