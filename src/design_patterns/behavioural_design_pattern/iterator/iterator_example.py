"""
Collection of Employees
list, set, dictionary, tree
One possibility for iterating over it

"""

from datetime import datetime


class Employee(object):
    def __init__(self, empid, name, hiredate):
        self.empid = empid
        self.name = name
        self.hiredate = hiredate


class Employees(object):

    _employees = {}
    _headcount = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def get_employee(self, i):
        return self._employees[i]

    @property
    def headcount(self):
        return self._headcount


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

TESTDEPARTMENTS = ()


if __name__ == "__main__":
    print("Employees:")

    for i in range(1, employees.headcount + 1):
        employee = employees.get_employee(i)
        print(
            "Employee Id: {}; Name: {}; Date of Hire: {}".format(
                employee.empid, employee.name, employee.hiredate
            )
        )
