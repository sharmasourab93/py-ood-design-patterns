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
        if value == 'myclass':
            return MyClass()
        else:
            return NullClass()


class NullClass(AbsClass):
    def do_something(self, value):
        print("Not Doing %s." % value)


if __name__ == '__main__':
    my_obj = MyObjectFactory.create_object('myotherclass')
    # my_obj = MyObjectFactory.create_object('myclass')
    my_obj.do_something('something')
