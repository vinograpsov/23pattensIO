from abc import abstractmethod, ABC

class NewsPaperPublisher:
    state = 0

    subscibers = []

    def subscribe(self,subscriber):
        self.subscibers.append(subscriber)
        print("you was subscribed")
    def unsubscribe(self,subscriber):
        self.subscibers.remove(subscriber)
        print("you was subscribed")
    def notifyAboutProduct(self):
        print("Start notifying")
        for subsciber in self.subscibers:
            subsciber.update(self)

    def printNewsPaper(self):
        if self.state == 1:
            self.state = 0
            print("print")
        else:
            self.state = 1
            print("print")
        self.notifyAboutProduct()
class Subscriber(ABC):
    @abstractmethod
    def update(self,newsPaperPublisher):
        pass

class Person:
    def update(self,newsPaperPublisher):
        if newsPaperPublisher.state == 1:
            print("nowa gazeta")

class MagazineShop:
    def update(self,newsPaperPublisher):
        if newsPaperPublisher.state == 1:
            print("nowa partia gazet")
if __name__ == "__main__":

    times = NewsPaperPublisher()

    person = Person()
    times.subscribe(person)

    magazineShop = MagazineShop()
    times.subscribe(magazineShop)

    times.printNewsPaper()

