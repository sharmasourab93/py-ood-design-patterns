"""
Python: Inheritance Vs Composition
        Follows Single Responsibility Principle
            keep objects simple,
            each object does only one thing.

Resource Reference:
https://realpython.com/inheritance-composition-python/#composition-in-python
https://stackoverflow.com/questions/20847727/python-inheritance-versus-composition
"""


class Person(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)


class Parent(Person):

    def __init__(self, firstname, lastname):
        super(Parent, self).__init__(firstname, lastname)
        self.kids = []

    def havechild(self, firstname):
        print(self.firstname, "is having a child")
        self.kids.append(Child(self, firstname))


class Child(Person):

    def __init__(self, parent, firstname):
        super(Child, self).__init__(firstname, parent.lastname)
        self.parent = parent
