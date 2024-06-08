"""
Interfaces in Python:
Interfaces stand for 'I' in SOLID i.e.
Interface Segregation Principle

Interfaces are supported in C++ using Abstract classes
Interface are supported in Java, C#, VB with interfacedef

Interfaces in Python appeared in PEP3119
First appeared in Python Version 2.6 & 3.0
"""

import abc


# Abstract Base class definition
class BaseClass(abc.ABC):

    def __init__(self):
        print("Base Class Constructor")

    # Abstract Method Definition
    @abc.abstractmethod
    def do_something(self, value):
        """
        An Abstract Method is a method
        which has to be implemented in
        derived class
        :param value: Value is a must in derived
        """
        pass

    # Abstract Property
    @abc.abstractproperty
    def some_property(self):
        """Required property in the derived class"""
        pass


# Derived class can be also
# referred to as Concrete Class Implementation
# Inheritance from Base Class
class DerivedClass(BaseClass):
    """Implementation of Derived Class"""

    def __init__(self):
        super().__init__()
        print("Extending Base Class Constructor in Derived Class.")

    def do_something(self, value):
        print("{} is being printed.".format(value))

    @property
    def some_property(self):
        """A Property must be implemented as
        declared abstract in the base class.
        """
        return "Property Validation"


if __name__ == "__main__":

    derived_obj = DerivedClass()

    print(derived_obj.do_something("Sourab"))
    print(derived_obj.some_property)
