# Proxy Pattern

The Proxy pattern places another object in front of the real object in order to control access or add extra behavior around it.

## Before: Data Access And Permission Logic Mixed Together

Source idea from `proxy_example.py`.

```python
def get_employee_info(empids, reqid):
    for empid in empids:
        ...
        if reqid in ACCESSCONTROL:
            if ACCESSCONTROL[reqid].can_see_personal:
                details += ", Birthdate: {}, Salary: {}".format(
                    employee.birthdate, employee.salary
                )
```

## After: Proxy Controls What The Caller Sees

Source idea from `proxy_applied.py`.

```python
class Proxy(AbsEmployees):
    def __init__(self, employees, reqid):
        self._employees = employees
        self._reqid = reqid

    def get_employee_info(self, empids):
        reqid = self._reqid
        acc = AccessControls.get_access_control()

        for e in self._employees.get_employee_info(empids):
            if e.empid == reqid or (reqid in acc and acc[reqid].can_see_personal):
                yield Employee(e.empid, e.name, ("%.2f" % e.salary), e.birthdate)
            else:
                yield Employee(e.empid, e.name, "*****", "*****")
```

## Takeaway

Use Proxy when access to the real object should be filtered, delayed, monitored, or otherwise controlled.
