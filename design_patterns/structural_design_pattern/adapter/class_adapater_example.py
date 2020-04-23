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


class Customer(object):
    def __init__(self, name, address):
        self._name = name
        self._address = address
    
    @property
    def name(self):
        return self._name
    
    @property
    def address(self):
        return self._address
    

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


class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
    
    @property
    def address(self):
        return "{} {}".format(
            self.number,
            self.street
            )


MOCK_VENDORS = (
    VendorAdapter("Dough Factory", 1, "Semolina Court"),
    VendorAdapter("Farm Produce", 14, "Country Road"),
    VendorAdapter("Cocoa World", 53, "Tropical Blvd")
)


CUSTOMERS = MOCK_VENDORS


if __name__ == '__main__':
    for cust in CUSTOMERS:
        print("Name: {}, Address: {}".format(
                                        cust.name,
                                        cust.address))
