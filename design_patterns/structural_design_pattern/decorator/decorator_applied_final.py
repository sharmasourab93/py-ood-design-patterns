import abc


class AbsCar(abc.ABC):
    @abc.abstractproperty
    def description(self):
        pass
    
    @abc.abstractproperty
    def cost(self):
        pass
    

class Economy(AbsCar):
    @property
    def description(self):
        return "Economy"
    
    @property
    def cost(self):
        return 12000.00


class Luxury(AbsCar):
    @property
    def description(self):
        return "Luxury"
    
    @property
    def cost(self):
        return 18000.00


class Sport(AbsCar):
    @property
    def description(self):
        return "Sport"
    
    @property
    def cost(self):
        return 15000.00