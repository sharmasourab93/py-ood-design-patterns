from ..decorator_applied_final import AbsCar


class AbsDecorator(AbsCar):
    def __init__(self, car):
        self._car = car

    # Composition takes place at run time
    @property
    def car(self):
        return self._car
