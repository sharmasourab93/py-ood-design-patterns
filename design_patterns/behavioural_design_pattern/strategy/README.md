# Strategy Pattern

The Strategy pattern places interchangeable algorithms behind a common interface. The caller chooses a strategy without rewriting the calling code.

## Before: Branch On Every Algorithm

Source idea from `strategy_pattern_violation.py`.

```python
class ShippingCost:
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError("Invalid Shipper %s", order.shipper)
```

## After: Delegate To A Strategy Object

Source idea from `stragegy_pattern_applied.py`.

```python
class AbsStrategy(ABC):
    @abstractmethod
    def calculate(self, order):
        pass


class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3


class ShippingCost:
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)
```

## Takeaway

Use Strategy when you have multiple ways to perform the same task and want the algorithm to vary independently of the calling code.
