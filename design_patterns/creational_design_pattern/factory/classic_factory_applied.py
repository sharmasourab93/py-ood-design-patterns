import abc


class AbsAuto(abc.ABC):

    def __init__(self, carname):
        self._carname = carname

    @abc.abstractmethod
    def start(self):
        pass

    @property
    def name(self):
        return self._carname

    @name.setter
    def name(self, name):
        self._name = name
        self._carname = name

    @abc.abstractmethod
    def stop(self):
        pass


class AbsFactory(abc.ABC):

    @abc.abstractmethod
    def create_auto(self):
        pass


class ChevyVolt(AbsAuto):
    def start(self):
        print("{} Running with  Shocking Power".format(self._carname))

    def stop(self):
        print("{} Shutting Down.".format(self._carname))


class ChevyFactory(AbsFactory):

    def create_auto(self):
        self.chevy = chevy = ChevyVolt("Chevy Volt")
        chevy.name = "Chevy Volt"
        return chevy
