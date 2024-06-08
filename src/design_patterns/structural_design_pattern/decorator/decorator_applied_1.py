"""Use properties
One conrete class per model
More properties to implmenet
more complicated constructor
maintainance
what is the option to change price?
    open up ABC?
    
Principles violated

SRP - aggregate cost calculations
OCP -
IFS -
DIP -
DRY -  
"""


import abc


class AbsCar(abc.ABC):
    @abc.abstractproperty
    def description(self):
        pass
    
    @abc.abstractproperty
    def engine(self):
        pass
    
    @abc.abstractproperty
    def paint(self):
        pass
    
    @abc.abstractproperty
    def upholstery(self):
        pass
    
    def cost(self):
        cost = 0.00
        if self.engine == "4 cyl":
            cost += 0.00
        elif self.engine == '6 cyl':
            cost += 1500.00
        
        if self.paint == 'white':
            cost += 0.00
        elif self.paint == 'black':
            cost += 1000.00
        elif self.paint == 'red':
            cost += 2000.00
        
        if self.upholstery == 'vinyl':
            cost += 0.00
        elif self.upholstery == 'leather':
            cost += 2000.00
            
        return cost
    
    
class Economy(AbsCar):
    def __init__(self, engine, paint, upholstery):
        self._engine = engine
        self._paint = paint
        self._upholstery = upholstery
        
    @property
    def description(self):
        return "Economy"
    
    @property
    def engine(self):
        return self._engine
    
    @property
    def paint(self):
        return self._paint
    
    @property
    def upholstery(self):
        return self._upholstery
    
    @property
    def cost(self):
        return 12000.00 + super().cost()


if __name__ == '__main__':
    car1 = Economy('4 cyl', 'black', 'vinyl')
    car2 = Economy('6 cyl', 'red', 'leather')
    
    print("{} : ${}".format(car1.description, car1.cost))
    print("{} : ${}".format(car2.description, car2.cost))