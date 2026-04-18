from .decorator_applied_final import Economy
from .decos.black import Black
from .decos.v6 import V6
from .decos.vinyl import Vinyl


def main():
    car = Economy()
    show(car)
    car = V6(car)
    show(car)
    car = Vinyl(car)
    show(car)
    car = Black(car)
    show(car)


def show(car):
    print("Description: {}; cost: ${}".format(car.description, car.cost))


if __name__ == "__main__":
    main()
