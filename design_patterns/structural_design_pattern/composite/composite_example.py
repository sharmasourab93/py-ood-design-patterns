from collections import Iterable
from datetime import date


class Person:
    name = None
    birthdate = None

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


class Family(Iterable):
    members = []

    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)


def main():
    family = Family(
        [
            Person("Trillian", date(1970, 3, 14)),
            Person("Arthur", date(1965, 7, 4)),
            Person("Ford", date(1995, 2, 2)),
            Person("Zaphod", date(1997, 5, 1)),
            Person("Douglas", date(1999, 4, 2)),
        ]
    )

    singles = [Person("Marvin", date(1991, 1, 1)), Person("Slarti", date(1993, 9, 9))]

    oldest = None
    earliest_date = date.max
    for m in family:
        if m.birthdate < earliest_date:
            oldest = m
            earliest_date = m.birthdate

    for s in singles:
        if s.birthdate < earliest_date:
            oldest = s
            earliest_date = s.birthdate

    max_age = (date.today() - earliest_date).days / 365.2425
    print("Oldest Person: {}; Age: {:6.2f}".format(oldest.name, max_age))


if __name__ == "__main__":
    main()
