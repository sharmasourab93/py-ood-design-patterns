# Bridge Pattern

The Bridge pattern separates an abstraction from its implementation so both can vary independently. This is useful when two different dimensions of change would otherwise create a class explosion.

## Example

Source idea from `bridge_example.py`.

```python
alert = Alert("Server CPU high", EmailSender())
alert.send()

alert = Alert("Build failed", SlackSender())
alert.send()
```

The message type stays the same while the delivery implementation changes.

## Takeaway

Use Bridge when you want to combine different abstractions with different implementations without creating one subclass for every combination.
