"""
Python
Don't Repeat Yourself principle violated.
"""


class Bus(object):
    
    def __init__(self, destination):
        self._destination = destination
        
    def bus_trip(self):
        self.start_diesel()
        self.leave_terminal()
        self.drive_to_destination()
        self.arrive_at_destination()
        
    def start_diesel(self):
        print("Starting the Cummins Diesel Engine")

    def leave_terminal(self):
        print("Leaving Terminal")

    def drive_to_destination(self):
        print("Driving ...")

    def arrive_at_destination(self):
        print("Arriving at " + self._destination)
        

class Airplane(object):
    def __init__(self, destination):
        self._destination = destination
        
    def plane_trip(self):
        self.start_gas_turbines()
        self.leave_terminal()
        self.fly_to_destination()
        self.land_at_destination()

    def start_gas_turbines(self):
        print("Starting the Rolls-Royce gas-turbine engines")

    def leave_terminal(self):
        print("Taxing to the runway")
        print("Taking off")

    def fly_to_destination(self):
        print("Flying...")

    def land_at_destination(self):
        print("Landing at" + self._destination)


def take_bus(destination):
    print("Taking the bus to " + destination + "==>")
    bus = Bus(destination)
    bus.bus_trip()

    
def take_plane(destination):
    print("Flying to " + destination + "==>")
    plane = Airplane(destination)
    plane.plane_trip()
    

if __name__ == '__main__':
    take_bus('New York')
    take_plane('Amsterdam')
