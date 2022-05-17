from abc import ABC, abstractmethod


class LogisticsCompany(ABC):
    def createTransport(self) :
        product = self.factory_method()
        result = f"{product.deliver()}"
        return result



class TruckLogistics(LogisticsCompany):
    def factory_method(self):
        return Truck()

class TrainLogistics(LogisticsCompany):
    def factory_method(self):
        return Train()

class PlainLogistics(LogisticsCompany):
    def factory_method(self):
        return Plain()



class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "delivered by truck"


class Train(Transport):
    def deliver(self):
        return "delivered by train"

class Plain(Transport):
    def deliver(self):
        return "delivered by plain"

def chooseDelivery(creator):
    print(f"{creator.createTransport()}")


if __name__ == "__main__":
    chooseDelivery(TruckLogistics())
    chooseDelivery(TrainLogistics())
    chooseDelivery(PlainLogistics())

