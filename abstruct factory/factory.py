from abc import ABC, abstractmethod


class ClothesFactory(ABC):
    @abstractmethod
    def makeTrouses(self):
        pass

    @abstractmethod
    def makeShirt(self):
        pass


class Zara(ClothesFactory):
    def makeTrouses(self):
        return ZaraTrouses()
    def makeShirt(self):
        return  ZaraShirt()

class Reserved(ClothesFactory):
    def makeTrouses(self):
        return ReservedTrouses()
    def makeShirt(self):
        return ReservedShirt()



class Shirt(ABC):
    @abstractmethod
    def brand(self):
        pass

class ZaraShirt(Shirt):
    def brand(self):
        return "Zara shirt"


class ReservedShirt(Shirt):
    def brand(self):
        return "Reserved shirt"


class Trouses(ABC):
    @abstractmethod
    def brand(self):
        pass


class ZaraTrouses(Trouses):
    def brand(self):
        return "Zara Trouses"


class ReservedTrouses(Trouses):
    def brand(self):
        return "Reserved Trouses"


def showClothes(brandFactory):
    trouses = brandFactory.makeTrouses()
    shirt = brandFactory.makeShirt()

    print(trouses.brand())
    print(shirt.brand())


if __name__ == "__main__":
    showClothes(Zara())
    showClothes(Reserved())