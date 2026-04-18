# Visitor Pattern

The Visitor pattern lets you add new operations to an existing object structure without modifying the element classes themselves.

## Example

Source idea from `visitor_example.py`.

```python
class Book:
    def accept(self, visitor):
        return visitor.visit_book(self)


class Food:
    def accept(self, visitor):
        return visitor.visit_food(self)
```

The operation lives in the visitor:

```python
class TaxVisitor:
    def visit_book(self, book):
        return book.price * 1.05

    def visit_food(self, food):
        return food.price * 1.02
```

Output:

```text
105.0
51.0
```

## Takeaway

Use Visitor when you need to add new operations over a stable set of object types without editing those types repeatedly.
