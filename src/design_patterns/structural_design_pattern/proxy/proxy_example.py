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
        

EMPLOYEES = {
    1: Employee(1, "Bob", "4 Jul 1994", 80000.00),
    2: Employee(2, "Carol", "28 May 1992", 85000.00),
    3: Employee(3, 'Ted', '18 Feb 1988', 55000.00),
    4: Employee(4, 'Alice', "25 Nov 1987", 40000.00),
    101: Employee(101, "Morgan The manager", "14 Mar 1975", 100000.00)
    }

ACCESSCONTROL = {
    101: AccessControl(101, True)
    }


def get_employee_info(empids, reqid):
    for empid in empids:
        if empid not in EMPLOYEES:
            continue
            
        employee = EMPLOYEES[empid]
        details = "Employee ID: {}, Name: {}".format(employee.empid, employee.name)
        
        if reqid in ACCESSCONTROL:
            if ACCESSCONTROL[reqid].can_see_personal:
                details += (", Birthdate: {}, Salary: {}"
                            .format(employee.birthdate, employee.salary))
        print(details)
        

if __name__ == '__main__':
    get_employee_info([3, 4], 3) # Requestor may not see personal data
    get_employee_info([1, 2], 101) # Requestor may see personal data