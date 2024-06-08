"""
Build iterators for the collections
Look at both types
Iterable = Iterator
"""

from collections import Iterable, Iterator, Sequence
from datetime import datetime


class Employee(object):
    def __init__(self, empid, name, hiredate):
        self.number = empid
        self.name = name
        self.date = hiredate


class Department(object):
    def __init__(self, deptid, name, date_established):
        self.number = deptid
        self.name = name
        self.date = date_established


class Employees(Iterable):
    _employees = {}
    _headcount = 0
    _empid = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        return EmployeesIterator(self._employees, self._headcount)


class EmployeesIterator(Iterator):
    def __init__(self, employees, headcount):
        self._employees = employees
        self._headcount = headcount
        self._empid = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._empid < self._headcount:
            self._empid += 1
            return self._employees[self._empid]
        else:
            raise StopIteration


class Departments(Sequence):
    _departments = []

    def add_department(self, department):
        self._departments.append(department)

    def __getitem__(self, item):
        return self._departments[item]

    def __len__(self):
        return len(self._departments)


TESTEMPLOYEES = (
    (1, "Douglas Adams", datetime(1942, 7, 6)),
    (2, "Sherlock Holmes", datetime(1887, 3, 15)),
    (3, "Albert Einstein", datetime(1915, 11, 25)),
    (4, "Sir John A McDonald", datetime(1867, 8, 1)),
    (5, "Theodore Roosevelt", datetime(1901, 9, 14)),
)

employees = Employees()
for empid, name, hiredate in TESTEMPLOYEES:
    employees.add_employee(Employee(empid, name, hiredate))

TESTDEPARTMENTS = (
    (101, "Sci-Fi Commedy", datetime(2010, 10, 1)),
    (102, "Mystery", datetime(2012, 2, 13)),
    (103, "Physics", datetime(2014, 5, 14)),
    (104, "Politics", datetime(2016, 7, 28)),
    (201, "POTUS", datetime(1776, 7, 4)),
)

departments = Departments()
for deptid, name, date_estb in TESTDEPARTMENTS:
    departments.add_department(Department(deptid, name, date_estb))


def print_summary(collection):
    for item in collection:
        print(
            "Item Id: {}; Name:{}; Dated: {}".format(item.number, item.name, item.date)
        )


if __name__ == "__main__":
    i1 = iter(employees)
    i2 = iter(employees)
    # assert i1 == i2

    for _ in range(5):
        print("{}, {}".format(next(i1).number, next(i2).number))
