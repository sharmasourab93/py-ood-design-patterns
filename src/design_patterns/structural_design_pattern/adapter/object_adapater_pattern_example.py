import abc


class AbsAdapter(abc.ABC):
    def __init__(self, adaptee):
        self._adaptee = adaptee
        
    @property
    def adaptee(self):
        return self._adaptee
    
    @abc.abstractproperty
    def name(self):
        pass
    
    @abc.abstractproperty
    def address(self):
        pass


class Vendor(object):
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street
    
    @property
    def name(self):
        return self._name
    
    @property
    def number(self):
        return self._number
    
    @property
    def street(self):
        return self._street


class VendAdapter(AbsAdapter):
    
    @property
    def name(self):
        return self.adaptee.name
    
    @property
    def address(self):
        return "{} {}".format(
            self.adaptee.number,
            self.adaptee.street
            )


MOCK_VENDORS = (
    VendAdapter(Vendor("Dough Factory", 1, "Semolina Court")),
    VendAdapter(Vendor("Farm Produce", 14, "Country Road")),
    VendAdapter(Vendor("Cocoa World", 53, "Tropical Blvd"))
)
CUSTOMERS =  MOCK_VENDORS


if __name__ == '__main__':
    for cust in CUSTOMERS:
        print("Name: {}, Address: {}".format(
                                        cust.name,
                                        cust.address))
