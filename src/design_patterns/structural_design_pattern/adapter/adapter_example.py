TYPE = 'vendors'


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


MOCK_CUSTOMERS = (
    Customer("Pizza Love", "33 Pepproni Lane"),
    Customer("Happy & Green", "25 Kale St."),
    Customer("Sweet Tooth", "42 Chocolate Ave.")
)


MOCK_VENDORS = (
    Vendor("Dough Factory", 1, "Semolina Court"),
    Vendor("Farm Produce", 14, "Country Road"),
    Vendor("Cocoa World", 53, "Tropical Blvd"),
)


if __name__ == '__main__':
    
    if TYPE == 'customers':
        for cust in MOCK_CUSTOMERS:
            print("Name: %s; Address: %s"% (cust.name, cust.address))
    elif TYPE == 'vendors':
        for vend in MOCK_VENDORS:
            print("Name: {}; Number: {}, {}; ".format(vend.name,
                                                    vend.number,
                                                    vend.street))
    
    else:
        raise ValueError('IncorrectType: ' + TYPE)
