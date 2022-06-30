from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def purchase(self):
        pass

class AppleLaptop(Laptop):
    def purchase(self):
        return "Compraste una Laptop Apple"

class HPLaptop(Laptop):
    def purchase(self):
        return "Compraste una Laptop HP "

class Tablet(ABC):
    @abstractmethod
    def purchase(self):
        pass

class AppleTablet(Tablet):
    def purchase(self):
        return "Compraste una Tablet Apple"

class HPTablet(Tablet):
    def purchase(self):
        return "Compraste una Tablet HP "

class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

class AppleFactory(DeviceFactory):
    def create_laptop(self):
        return AppleLaptop()
    
    def create_table(self):
        return AppleTablet()

class HPFactory(DeviceFactory):
    def create_laptop(self):
        return HPLaptop()
    
    def create_table(self):
        return HPTablet()

if __name__ == "__main__":
    factory = HPFactory()
    tablet = factory.create_laptop()
    print(tablet.purchase())