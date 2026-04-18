# Interface Segregation Principle

The Interface Segregation Principle says clients should not be forced to depend on methods they do not need. Smaller, role-based interfaces are easier to use and easier to implement correctly.

## Problem Shape

Source idea from `inteface_segregation_principle.py`.

```python
class BankAccount:
    def deposit(self):
        pass

    def balance(self):
        pass

    def withdraw(self):
        pass
```

This broad interface is then narrowed into more specific roles:

```python
class OnlyWithdrawOperator:
    def withdraw(self):
        pass

    def balance(self):
        pass


class OnlyDepositOperator:
    def deposit(self):
        pass


class POS(OnlyDepositOperator):
    pass
```

## What To Notice

- not every client needs deposit, withdraw, and balance together
- role-specific interfaces reduce unnecessary dependency
- a POS device only needs deposit behavior, so it should not depend on withdraw behavior

## Repository Note

This file is more of a concept sketch than a complete runnable implementation, but it still captures the core idea clearly.

## Takeaway

If a client uses only one small part of a large interface, the interface is probably too broad.
