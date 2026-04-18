# Observer Pattern

The Observer pattern defines a one-to-many dependency between objects. When one object changes, all subscribed observers can be notified automatically.

## Before: Reporting Logic Is Hard-Coded

Source idea from `kpi_data_before.py`.

```python
for kpi in KPI_Data:
    if kpi.name == "open":
        print("Current open Tickets: %s" % kpi.value)
    elif kpi.name == "new":
        print("New Tickets in last hour: %s" % kpi.value)
    elif kpi.name == "closed":
        print("Tickets closed in last hour: %s" % kpi.value)
```

## After: Subject Notifies Observers

Source idea from `kpi_data_after.py`.

```python
class AbsSubject(object):
    _observer = set()

    def attach(self, observer):
        self._observer |= {observer}

    def notify(self, value=None):
        for observer in self._observer:
            observer.update()
```

Concrete observer:

```python
class CurrentKPIs(AbsObserver):
    def update(self, value=None):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()
```

## Takeaway

Observer is useful when multiple views or reactions depend on the same changing state.
