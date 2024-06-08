""""
OPEN CLosed
Dependency Inversion Principle
"""

class ChevyVolt(object):
    def start(self):
        print("Chevrolet Volt Running with  Shocking Power")
    
    def stop(self):
        print("Chevrolet Volt Shutting Down.")


class FordFocus:
    def start(self):
        print("Ford Focus Running with  Shocking Power")
    
    def stop(self):
        print("Ford Focus Shutting Down.")


class JeepSahara:
    def start(self):
        print("Jeep Sahara Running with  Shocking Power")
    
    def stop(self):
        print("Jeep Sahara Shutting Down.")


class NullCar:
    def __init__(self, carname):
        self._carname = carname
        
    def start(self):
        print("Unknown car {0}".format(self._carname))
    
    def stop(self):
        pass


# RED FLAG
def getcar(carname):
    if carname == "Chevy":
        return ChevyVolt()
    elif carname == "Ford":
        return FordFocus()
    elif carname == "Jeep":
        return JeepSahara()
    else:
        return NullCar(carname)
    

if __name__ == '__main__':
    for carname in ['Chevy', 'Ford', 'Jeep', 'Tesla']:
        car = getcar(carname)
        car.start()
        car.stop()
