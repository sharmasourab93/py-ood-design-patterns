import abc


# ABC Base Observer class
class AbsObserver(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# ABC Base Subject class
class AbsSubject(object):
    __metaclass__ = abc.ABCMeta
    _observer = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("Observer not derived from AbsObserver")
        self._observer |= {observer}

    def detach(self, observer):
        self._observer -= {observer}

    def notify(self, value=None):
        for observer in self._observer:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observer.clear()


class KPIs(AbsSubject):
    _open_ticket = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_ticket

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_ticket = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()


class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value=None):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print("Current Open Tickets: {}".format(self.open_tickets))
        print("New Tickets in last hour: {}".format(self.closed_tickets))
        print("Tickets closed in last hour: {}".format(self.new_tickets))
        print("*****", end="\n\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)


class ForecastKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value=None):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print("Forecast Open Tickets: {}".format(self.open_tickets))
        print("New Tickets in next hour: {}".format(self.closed_tickets))
        print("Tickets closed in next hour: {}".format(self.new_tickets))
        print("*****", end="\n\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)


if __name__ == "__main__":

    with KPIs() as kpis:
        with CurrentKPIs(kpis), ForecastKPIs(kpis):
            kpis.set_kpis(25, 10, 5)
            kpis.set_kpis(100, 50, 30)
            kpis.set_kpis(50, 10, 20)

    print("\n*** Exited Context Managers. ***\n\n")
    kpis.set_kpis(150, 110, 120)
