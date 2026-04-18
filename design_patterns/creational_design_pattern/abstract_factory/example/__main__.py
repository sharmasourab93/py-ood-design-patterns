from random import randint

from factories.ford import FordFiesta, FordMustang, LincolnMKS
from factories.gm import CadillacCTS, ChevyCamaro, ChevySpark

makers = ("gm", "ford")
editions = ("Econonmy", "Sport", "Luxury")
maker = makers[randint(0, 1)]
edition = editions[randint(0, 2)]

if maker == "gm":
    if edition == "Econonmy":
        car = ChevySpark()
    elif edition == "Sport":
        car = ChevyCamaro()
    elif edition == "Luxury":
        car = CadillacCTS()
    else:
        raise ValueError("Unknown car")
elif maker == "ford":
    if edition == "Econonmy":
        car = FordFiesta()
    elif edition == "Sport":
        car = FordMustang()
    elif edition == "Luxury":
        car = LincolnMKS()
    else:
        raise ValueError("Unknown car.")
else:
    raise ValueError("Unknown maker.")

car.start()
car.stop()
