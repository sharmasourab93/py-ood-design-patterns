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


class Economy4CylWhiteVinyl(Economy):
    @property
    def description(self):
        return "Economy, White, 4 cylinder, vinyl upholstery"

    @property
    def cost(self):
        return 12000.00


class Economy6CylWhiteVinyl(Economy):

    @property
    def description(self):
        return "Economy, 6 cylinder, White Vinyl, Upholstery"

    @property
    def cost(self):
        return 13500.00


if __name__ == "__main__":
    car1 = Economy4CylWhiteVinyl()
    car2 = Economy6CylWhiteVinyl()
    print(car1.description, car1.cost)
    print(car2.description, car2.cost)
