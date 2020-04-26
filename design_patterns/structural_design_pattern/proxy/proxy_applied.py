import abc


class AbsEmployees(abc.ABC):
    
    @abc.abstractmethod
    def get_employee_info(self, empids):
        pass


class Employee:
    def __init__(self, empid, name, birthdate, salary):
        self.empid = empid
        self.name = name
        self.birthdate = birthdate
        self.salary = salary


class AccessControl:
    def __init__(self, empid, can_see_personal):
        self.empid = empid
        self.can_see_personal = can_see_personal


class Employees(AbsEmployees):
    
    def get_employee_info(self, empids):
        
        return (EMPLOYEES[empid]
                for empid in empids
                if empid in EMPLOYEES
                )


class AccessControls:
    @staticmethod
    def get_access_control():
        return ACCESSCONTROL


class Proxy(AbsEmployees):
    def __init__(self, employees, reqid):
        self._employees = employees
        self._reqid = reqid
        
    def get_employee_info(self, empids):
        reqid = self._reqid
        acc = AccessControls.get_access_control()
        
        for e in self._employees.get_employee_info(empids):
            if e.empid == reqid or \
                    (reqid in acc and acc[reqid].can_see_personal):
                # Show everything
                yield Employee(e.empid, e.name,
                               ("%.2f" % e.salary),
                               e.birthdate
                               )
            else: # Hide birth date and salary details
                yield Employee(e.empid, e.name, "*****", "*****")
                
            
ACCESSCONTROL = {
    101: AccessControl(101, True)
    }


EMPLOYEES = {
    1: Employee(1, "Bob", "4 Jul 1994", 80000.00),
    2: Employee(2, "Carol", "28 May 1992", 85000.00),
    3: Employee(3, 'Ted', '18 Feb 1988', 55000.00),
    4: Employee(4, 'Alice', "25 Nov 1987", 40000.00),
    101: Employee(101, "Morgan The manager", "14 Mar 1975", 100000.00)
    }


def get_employees_Connection(reqid):
    return Proxy(Employees(), reqid)

DETAILS = "Employee ID: %d, Name: %s, Birthdate: %s, Salary: %s"


def print_employee_details(empids, reqid):
    employees = get_employees_Connection(reqid)
    for e in employees.get_employee_info(empids):
        print(DETAILS % (
                e.empid,
                e.name,
                e.birthdate,
                e.salary)
              )
    
        
if __name__ == '__main__':
    print("Requestor authorized to see everything:")
    print_employee_details([1, 2], 101)
    print("Requestor is an ordinary employee.")
    print_employee_details([1, 2, 3, 4], 3)
