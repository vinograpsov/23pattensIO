from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def make_walls(self):
        pass

    @abstractmethod
    def make_roof(self):
        pass

    @abstractmethod
    def make_door(self):
        pass

    @abstractmethod
    def make_windows(self):
        pass

    @abstractmethod
    def make_garage(self):
        pass

class HouseBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Building()

    def product(self):
        product = self._product
        self.reset()
        return product

    def make_walls(self):
        self._product.build_part("Simple walls were built")

    def make_roof(self):
        self._product.build_part("Simple roof was built")

    def make_door(self):
        self._product.build_part("Simple door was built")

    def make_windows(self):
        self._product.build_part("Simple windows were built")

    def make_garage(self):
        self._product.build_part("Simple garage was built")


class OfficeCenterBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Building()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def make_walls(self):
        self._product.build_part("Simple walls were built")

    def make_roof(self):
        self._product.build_part("Simple roof was built")

    def make_door(self):
        self._product.build_part("Simple door was built")

    def make_windows(self):
        self._product.build_part("Large windows to the floor were built")

    def make_garage(self):
        self._product.build_part("Simple garage was built")

class MansionBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Building()

    def product(self):
        product = self._product
        self.reset()
        return product

    def make_walls(self):
        self._product.build_part("Expensive walls were built")

    def make_roof(self):
        self._product.build_part("Expensive roof was built")

    def make_door(self):
        self._product.build_part("Expensive door was built")

    def make_windows(self):
        self._product.build_part("Expensive windows were built")

    def make_garage(self):
        self._product.build_part("Expensive garage was built")

class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder


    def built_simple_building(self):
        self.builder.make_walls()
        self.builder.make_roof()
        self.builder.make_windows()
        self.builder.make_door()

    def build_complete_building(self):
        self.builder.make_walls()
        self.builder.make_roof()
        self.builder.make_windows()
        self.builder.make_door()
        self.builder.make_garage()


class Building:
    def __init__(self):
        self.parts = []

    def build_part(self, part: Any):
        self.parts.append(part)

    def build_history(self):
        print(f"History of building: {', '.join(self.parts)}", end="")



if __name__ == "__main__":
    builderHouse = HouseBuilder()
    builderMansion = MansionBuilder()
    builderOffice = OfficeCenterBuilder()

    print("lets try to build simple house")
    builderHouse.make_roof()
    builderHouse.make_walls()
    builderHouse.make_door()
    builderHouse.make_windows()
    builderHouse.product().build_history()
    print()
    print("Stop... How we made how we made the roof before walls \n")

    print("lets try to use director")
    director = Director()
    director.builder = builderMansion
    director.build_complete_building()
    builderMansion.product().build_history()