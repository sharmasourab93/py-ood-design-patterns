# Chain of Responsibility Pattern

The Chain of Responsibility pattern passes a request through a chain of handlers until one of them can process it. This keeps the sender independent of the exact receiver.

## Example

Source idea from `chain_of_responsibility_example.py`.

```python
class SupportHandler:
    def handle(self, request):
        if self.can_handle(request):
            self.process(request)
            return
        if self._successor is not None:
            self._successor.handle(request)
            return
```

Concrete handlers implement only their own rule:

```python
class BillingHandler(SupportHandler):
    def can_handle(self, request):
        return request.issue_type == "billing"
```

Usage:

```python
support_chain.handle(SupportRequest("Alice", "billing", "Refund request"))
support_chain.handle(SupportRequest("Dave", "general", "Need help"))
```

Output:

```text
Billing handled request for Alice
No handler found for: general
```

## Takeaway

Use Chain of Responsibility when multiple objects may handle the same request and the sender should not know which one will do it.
