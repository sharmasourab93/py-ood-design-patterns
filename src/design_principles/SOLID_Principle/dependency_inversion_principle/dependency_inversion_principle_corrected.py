class Employee(object):
    def work(self):
        pass


class Manager:
    def __init__(self):
        self.employees = []

    def add_employee(self, a):
        self.employees.append(a)


class Developer(Employee):
    def __init__(self):
        print("developer added")

    def work(self):
        print("turning coffee into code")


class Designer(Employee):
    def __init__(self):
        print("designer added")

    def work(self):
        print("turning lines to wireframes")


class Testers(Employee):
    def __init__(self):
        print("tester added")

    def work(self):
        print("testing everything out there")


if __name__ == "__main__":
    a = Manager()
    a.add_employee(Developer())
    a.add_employee(Designer())
