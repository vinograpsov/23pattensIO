from __future__ import annotations
from abc import ABC, abstractmethod

class CarModel:
    def __init__(self, equipment, model):
        self.model = model
        self.equipment = equipment

    def name_model(self):
        return f"model: {self.model} {self.equipment.which_equipment()}"


class ConcreteModel(CarModel):
    def name_model(self):
        return f"model: {self.model} {self.equipment.which_equipment()} "


class Equipment(ABC):
    @abstractmethod
    def which_equipment(self):
        pass


class CheapEquipment(Equipment):
    def which_equipment(self):
        return "cheap equipment"


class MediumEquipment(Equipment):
    def which_equipment(self):
        return "medium equipment"


class FullEquipment(Equipment):
    def which_equipment(self):
        return "full equipment"


if __name__ == "__main__":
    cheapEquipment = CheapEquipment()
    mediumEquipment = MediumEquipment()
    fullEquipment = FullEquipment()

    volkswagenGolfCheap = ConcreteModel(cheapEquipment, "volkswagen golf")
    volkswagenGolfMedium = ConcreteModel(mediumEquipment, "volkswagen golf")
    volkswagenGolfFull = ConcreteModel(fullEquipment, "volkswagen golf")

    print(volkswagenGolfCheap.name_model())
    print(volkswagenGolfMedium.name_model())
    print(volkswagenGolfFull.name_model())









