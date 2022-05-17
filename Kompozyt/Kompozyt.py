from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class ArmyPartComponent(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    @abstractmethod
    def showPart(self):
        pass


class Person(ArmyPartComponent):
    def setName(self,name):
        self.name = name
    def showPart(self):
        return self.name


class ArmyPartContainer(ArmyPartComponent):
    def __init__(self):
        self._children = []

    def setName(self,name):
        self.name = name

    def add(self, component: ArmyPartComponent):
        self._children.append(component)
        component.parent = self

    def remove(self, component):
        self._children.remove(component)
        component.parent = None

    def showPart(self):
        results = []
        for child in self._children:
            results.append(child.showPart())
        return f"{self.name}({'+'.join(results)})"



if __name__ == "__main__":
    sniper = Person()
    sniper.setName("sniper")
    trooper = Person()
    trooper.setName("trooper")

    battalion = ArmyPartContainer()

    squad1 = ArmyPartContainer()
    squad2 = ArmyPartContainer()

    squad1.add(sniper)
    squad1.add(sniper)

    squad2.add(trooper)
    squad2.add(trooper)

    squad1.setName("squad1")
    squad2.setName("squad2")

    battalion.add(squad1)
    battalion.add(squad2)

    battalion.setName("battalion")

    print(battalion.showPart())
    print(squad1.showPart())