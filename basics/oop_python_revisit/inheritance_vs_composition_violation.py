"""
Python: Inheritance Vs Composition
        This Code Explains where Inheritance is not a good practise
        And How to implement the OOD Concept Composition
"""


class Parent:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.kids = []

    def havechild(self, firstname):
        print("{} is having a child".format(self.firstname))
        self.kids.append(Child(self, firstname))


# Derived Class of Parent
class Child(Parent):
    # Overriding Parent's __init__ Constructor
    def __init__(self, firstname, parent):
        self.parent = parent
        self.firstname = firstname
        self.lastname = parent.lastname
        
        
"""It is definitely not good to inherit Child from Parent or
    Parent from Child.
   The correct way to do it is to make a base class,
    let's say Person and inherit both Child and Parent from it.
   An advantage of doing this is to remove code repetition,
   at the moment you have only firstname /
   lastname fields copied into both objects,
   but you may have more data or additional methods,
   like get_name() to work with this data.
"""