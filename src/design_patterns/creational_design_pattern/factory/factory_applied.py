import abc
import sys
from inspect import getmembers, isabstract, isclass


class AbsAuto(abc.ABC):

    def __init__(self, carname):
        self._carname = carname

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class ChevyVolt(AbsAuto):
    def start(self):
        print("{} running with a shocking power!".format(self._carname))

    def stop(self):
        print("{} shutting down.".format(self._carname))


class FordFocus(AbsAuto):
    def start(self):
        print("{} running with a shocking power!".format(self._carname))

    def stop(self):
        print("{} shutting down.".format(self._carname))


class JeepSahara(AbsAuto):
    def start(self):
        print("{} running with a shocking power!".format(self._carname))

    def stop(self):
        print("{} shutting down.".format(self._carname))


class NullCar(AbsAuto):
    def start(self):
        print("{} Car Unknown".format(self._carname))

    def stop(self):
        pass


class AutoFactory(object):
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(sys.modules[__name__], isclass)
        abs_class = getmembers(sys.modules[__name__], isabstract)
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, abs_class[0][1]):
                self.autos.update([[name, _type]])
        print(self.autos)

    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname](carname)
        else:
            return self.autos["NullCar"](carname)


if __name__ == "__main__":
    factory = AutoFactory()
    for carname in ("ChevyVolt", "FordFocus", "JeepSahara", "Tesla 90D"):
        car = factory.create_instance(carname)
        car.start()
        car.stop()
