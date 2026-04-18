"""

"""

import abc


class AbsTransport(metaclass=abc.ABCMeta):
    def __init__(self, destination):
        self._destination = destination

    def take_trip(self):
        self.start_engine()
        self.leave_terminal()
        self.entertainment()
        self.travel_to_destination()
        self.arrive_at_destination()

    @abc.abstractmethod
    def start_engine(self):
        pass

    # Is Concrete method but can be implmented
    def leave_terminal(self):
        print("Leaving Terminal")

    # Hook Method
    def entertainment(self):
        pass

    @abc.abstractmethod
    def travel_to_destination(self):
        print("Travelling...")

    # Can be overridden
    def arrive_at_destination(self):
        print("Arriving at " + self._destination)


class Airplane(AbsTransport):
    def start_engine(self):
        print("Starting the Rolls-Royce gas turbine engines")

    def leave_terminal(self):
        print("Leaving terminal")
        print("Taxiing to Runway")

    def travel_to_destination(self):
        print("Flying...")

    # Hook Method
    def entertainment(self):
        print("Playing in-flight movies")

    def arrive_at_destination(self):
        print("Landing at" + self._destination)


class Bus(AbsTransport):
    def start_engine(self):
        print("Starting the Cummins Diesel engine")

    def travel_to_destination(self):
        print("Driving")


def travel(destination, transport):
    print(("Taking the {} to {}" + "===>").format(transport.__name__, destination))
    means = transport(destination)
    means.take_trip()


if __name__ == "__main__":
    travel("New York", Bus)
    travel("Amsterdam", Airplane)
