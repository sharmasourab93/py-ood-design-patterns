# Memento Pattern

The Memento pattern captures an object's state so it can be restored later without exposing the object's internal implementation details.

## Example

Source idea from `memento_example.py`.

```python
class TextEditor:
    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento):
        self.content = memento.content
```

History keeps saved snapshots:

```python
history.push(editor.save())
editor.write(" + Draft 2")
editor.restore(history.pop())
```

Output:

```text
Draft 1 + Draft 2
Draft 1
```

## Takeaway

Use Memento when you need undo, rollback, or snapshot behavior without exposing too much internal state.
