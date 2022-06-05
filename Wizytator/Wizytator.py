from __future__ import annotations
from abc import ABC, abstractmethod

class insuranceClient(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Person(insuranceClient):
    def accept(self, visitor: Visitor):
        visitor.visit_person(self)

    def who_am_i(self):
        return "i am person"


class House(insuranceClient):
    def accept(self, visitor: Visitor):
        visitor.visit_house(self)

    def who_am_i(self):
        return "i am house"


class Bank(insuranceClient):
    def accept(self, visitor: Visitor):
        visitor.visit_bank(self)

    def who_am_i(self):
        return "i am bank"



class Visitor(ABC):
    @abstractmethod
    def visit_person(self, element: Person):
        pass

    @abstractmethod
    def visit_house(self, element: House):
        pass

    @abstractmethod
    def visit_bank(self, element: Bank):
        pass


class cheapInsuranseVisitor(Visitor):
    def visit_person(self, element: Person):
        print(f"{element.who_am_i()} - cheap insuranse offer")

    def visit_house(self, element: House):
        print(f"{element.who_am_i()} - cheap insuranse offer")

    def visit_bank(self, element: Bank):
        print(f"{element.who_am_i()} - cheap insuranse offer")

class mediumInsuranseVisitor(Visitor):
    def visit_person(self, element: Person):
        print(f"{element.who_am_i()} - medium insuranse offer")

    def visit_house(self, element: House):
        print(f"{element.who_am_i()} - medium insuranse offer")

    def visit_bank(self, element: Bank):
        print(f"{element.who_am_i()} - medium insuranse offer")


class expensiveInsuranseVisitor(Visitor):
    def visit_person(self, element: Person):
        print(f"{element.who_am_i()} - expensive insuranse offer")

    def visit_house(self, element: House):
        print(f"{element.who_am_i()} - expensive insuranse offer")

    def visit_bank(self, element: Bank):
        print(f"{element.who_am_i()} - expensive insuranse offer")



if __name__ == "__main__":
    cheapOffer = cheapInsuranseVisitor()
    mediumOffer = mediumInsuranseVisitor()
    expensiveOffer = expensiveInsuranseVisitor()

    person = Person()
    house = House()
    bank = Bank()

    person.accept(cheapOffer)
    person.accept(mediumOffer)
    person.accept(expensiveOffer)

    house.accept(cheapOffer)
    house.accept(mediumOffer)
    house.accept(expensiveOffer)

    bank.accept(cheapOffer)
    bank.accept(mediumOffer)
    bank.accept(expensiveOffer)


