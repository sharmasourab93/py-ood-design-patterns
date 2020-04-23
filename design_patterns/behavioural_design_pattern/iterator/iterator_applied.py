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


class Department(object):
    def __init__(self, deptid, name, date_established):
        self.deptid = deptid
        self.name = name
        self.date_established = date_established


class Departments(object):
    _departments = []
    
    def add_department(self, department):
        self._departments.append(department)
        
    def get_department(self, i):
        return self._departments[i]
    
    @property
    def departments_range(self):
        return (0, len(self._departments)-1)


def print_summary(collection):
    pass


TESTEMPLOYEES = (
    (1, 'Douglas Adams', datetime(1942, 7, 6)),
    (2, "Sherlock Holmes", datetime(1887, 3, 15)),
    (3, "Albert Einstein", datetime(1915, 11, 25)),
    (4, "Sir John A McDonald", datetime(1867, 8, 1)),
    (5, "Theodore Roosevelt", datetime(1901, 9, 14))
    )

employees = Employees()
for empid, name, hiredate in TESTEMPLOYEES:
    employees.add_employee(Employee(empid, name, hiredate)
                           )

TESTDEPARTMENTS = (
    (101, 'Sci-Fi Commedy', datetime(2010, 10, 1)),
    (102, 'Mystery', datetime(2012, 2, 13)),
    (103, 'Physics', datetime(2014, 5, 14)),
    (104, 'Politics', datetime(2016, 7, 28)),
    (201, 'POTUS', datetime(1776, 7, 4))
)

departments = Departments()
for deptid, name, date_estb in TESTDEPARTMENTS:
    departments.add_department(Department(deptid, name, date_estb))
    

if __name__ == '__main__':
    print("Employees")
    for i in range(1, employees.headcount + 1):
        employee = employees.get_employee(i)
        print("Employee Id: {}; Name: {}; Date of Hire: {}"
              .format(employee.empid, employee.name, employee.hiredate)
              )
        
    print("Departments:")
    
    for i in range(*departments.departments_range):
        dept = departments.get_department(i)
        print("Department Id: {}; Name: {}; Date Established: {}"
              .format(dept.deptid, dept.name, dept.date_established)
              )
    print_summary(employees)
    print_summary(departments)
 