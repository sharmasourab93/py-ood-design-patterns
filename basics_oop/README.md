# Basics OOP

This folder should work as a quick Python OOP revision sheet. The examples below use actual code from this folder, trimmed down to the key idea, followed by the observed output.

## 1. Instance Method vs Class Method vs Static Method

Python supports three common method types inside a class. The difference is based on what context the method receives automatically: the object, the class, or neither.

Source idea from `oop_methods.py`.

```python
class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def class_method(cls):
        return "cls method called", cls

    @staticmethod
    def static_method():
        return "static method called"
```

How it is used:

```python
m = MyClass()

print(m.method())
print(m.class_method())
print(MyClass.static_method())
```

Output:

```text
('instance method called', <__main__.MyClass object at ...>)
('cls method called', <class '__main__.MyClass'>)
static method called
```

Key point:

- Instance method uses `self`.
- Class method uses `cls`.
- Static method uses neither.

## 2. Class Methods As Alternate Constructors

Class methods are often used to create well-named alternate ways of building an object. This keeps object creation readable and intention-revealing.

Source idea from `oop_cls_example.py`.

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return " ".join(self.ingredients)

    @classmethod
    def margherita(cls):
        return cls(["mozarella", "tomotoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozarella", "tomatoes", "ham"])
```

Usage:

```python
print(Pizza.margherita())
print(Pizza.prosciutto())
```

Output:

```text
mozarella tomotoes
mozarella tomatoes ham
```

Key point:

- Class methods are often used to create named construction paths.

## 3. Property And Setter

Properties let a method behave like an attribute. This is useful when you want clean access syntax without losing control over validation or internal updates.

Source idea from `oop_property_decorator.py`.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
```

Usage:

```python
emp1 = Employee("John", "Smith")
print(emp1.fullname)

emp1.fullname = "Corey Schafer"
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
```

Output:

```text
John Smith
Corey
Corey.Schafer@email.com
Corey Schafer
```

Key point:

- `fullname` looks like an attribute, but assignment triggers custom logic.

## 4. Basic Inheritance

Inheritance is used when one class is a specialized form of another. A child class inherits common behavior from the parent and can override selected parts.

Source idea from `inheritance_explained.py`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True
```

Usage:

```python
emp = Person("Geeks1")
print(emp.get_name())
print(emp.is_employee())

emp1 = Employee("Geeks2")
print(emp1.get_name())
print(emp1.is_employee())
print(isinstance(emp1, Person))
```

Output:

```text
Geeks1
False
Geeks2
True
True
```

Key point:

- `Employee` inherits from `Person` and overrides behavior.

## 5. Inheritance With Shared And Specialized Behavior

This example expands the inheritance idea by showing how a base class can capture shared state and behavior, while subclasses add only their specific details.

Source idea from `inheritance_again.py`.

```python
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{}"'.format(self.salary))
```

Output from the full file:

```text
Name:"Mrs. Shri Vidya" Age:"40" Salary:"30000"
Name:"Sourab" Age:"25" Marks: 80
```

Key point:

- Child classes reuse base behavior and add only what is specific to them.

## 6. Abstract Base Class

Abstract base classes are useful when you want to define a common contract and force child classes to implement required methods or properties.

Source idea from `abstract_interface.py`.

```python
import abc

class BaseClass(abc.ABC):
    @abc.abstractmethod
    def do_something(self, value):
        pass

    @abc.abstractproperty
    def some_property(self):
        pass


class DerivedClass(BaseClass):
    def do_something(self, value):
        print("{} is being printed.".format(value))

    @property
    def some_property(self):
        return "Property Validation"
```

Usage:

```python
derived_obj = DerivedClass()
print(derived_obj.do_something("Sourab"))
print(derived_obj.some_property)
```

Output:

```text
Sourab is being printed.
None
Property Validation
```

Key point:

- The derived class must implement every abstract member from the base class.

## 7. Class Variable vs Instance Variable

Class variables belong to the class itself, while instance variables belong to a single object. This example is useful for understanding shared state versus object-specific state.

Source idea from `oop_class_member.py`.

```python
class CSStudent:
    stream = "cse"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
```

Usage:

```python
a = CSStudent("Geek", 1)
b = CSStudent("Nerd", 2)

CSStudent.stream = "Cse"
a.stream = "ece"
```

Observed effect:

```text
Initially
a.stream= cse
b.stream= cse

Later
a.stream= ece
b.stream= Cse
```

Key point:

- Changing the class variable affects shared state.
- Assigning `a.stream` creates an instance-level override only for `a`.

## 8. Data Hiding And Name Mangling

Python does not enforce strict private fields in the same way as some other languages, but name mangling helps reduce accidental access to internal members.

Source idea from `oop_data_hiding.py`.

```python
class MyClass:
    __hidden = 0

    def add(self, increment):
        self.__hidden += increment
        print(self.__hidden)
```

Usage:

```python
my_class_obj = MyClass()
my_class_obj.add(2)
my_class_obj.add(10)
print(my_class_obj._MyClass__hidden)
```

Output:

```text
2
12
12
```

Key point:

- `__hidden` is name-mangled, not truly private.

## 9. __str__ vs __repr__

Python objects can define two different string representations: one for human-friendly display and another for developer-facing inspection.

Source idea from `oop_string_representation.py`.

```python
class Test:
    def __repr__(self):
        return "Test a:{} b:{}".format(self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s,b is %s" % (self.a, self.b)
```

Usage:

```python
test_obj = Test(1234, 5678)
print(test_obj)
print([test_obj])
```

Output:

```text
From str method of Test: a is 1234,b is 5678
[Test a:1234 b:5678]
```

Key point:

- `print(obj)` prefers `__str__`.
- Containers like lists typically show `__repr__`.

## 10. Inheritance vs Composition

One of the most important object modeling decisions is whether a relationship should be expressed through inheritance or through composition. This example shows why that distinction matters.

Bad modeling idea from `inheritance_vs_composition_violation.py`:

```python
class Parent:
    ...

class Child(Parent):
    ...
```

Better modeling idea from `inheritance_vs_composition_applied.py`:

```python
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Parent(Person):
    def __init__(self, firstname, lastname):
        super(Parent, self).__init__(firstname, lastname)
        self.kids = []

    def havechild(self, firstname):
        self.kids.append(Child(self, firstname))


class Child(Person):
    def __init__(self, parent, firstname):
        super(Child, self).__init__(firstname, parent.lastname)
        self.parent = parent
```

Key point:

- A child is not a type of parent.
- A parent has children, so composition is the better fit here.

## Summary

- Use instance methods when behavior depends on object state.
- Use class methods for class-aware logic or alternate constructors.
- Use static methods for utility behavior tied to a class domain.
- Use inheritance for real subtype relationships.
- Use composition when one object contains or depends on another.
- Use properties to keep attribute-style access with controlled behavior.
- Use `__str__` for readable display and `__repr__` for developer-facing representation.
