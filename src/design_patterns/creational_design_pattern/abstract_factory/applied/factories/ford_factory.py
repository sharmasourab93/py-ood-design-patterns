from autos.ford.fiesta import FordFiesta
from autos.ford.lincoln import LincolnMKS
from autos.ford.mustang import FordMustang

from .abs_factory import AbsFactory


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()
