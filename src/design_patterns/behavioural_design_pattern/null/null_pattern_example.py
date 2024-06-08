import abc


class AbsClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_something(self, value):
        pass


class MyClass(AbsClass):
    def do_something(self, value):
        print("Doing %s" % value)


class MyObjectFactory:
    @staticmethod
    def create_object(value):
        if value == "myclass":
            return MyClass()
        else:
            return None


if __name__ == "__main__":
    # myobj = MyObjectFactory.create_object('myotherclass')
    myobj = MyObjectFactory.create_object("myclass")
    if myobj is not None:
        myobj.do_something("something")
    else:
        print("Not doing anything")
