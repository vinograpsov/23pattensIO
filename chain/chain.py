from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class answeringMachineHandler(AbstractHandler):
    def handle(self, request):
        if request == "1":
            print(f"Client: {request}")
            return "You pushed number 1, you will be connected with call centre"
        elif request == "2":
            print(f"Client: {request}")
            return "You pushed number 2, you will be connected with manager"
        else:
            return super().handle(request)




class callCentreHandler(AbstractHandler):
    def handle(self, request):
        if request == "Yes":
            print("have you tried to reboot your device ?")
            print(f"Client: {request}")
            return "Hmmm... so unusual problem, we will connect you with IT specialist"
        elif request == "No":
            print("have you tried to reboot your device ?")
            print(f"Client: {request}")
            return "just reboot your device and dont call us if you didnt make reboot"
        else:
            return super().handle(request)




class ITSpecialistHandler(AbstractHandler):
    def handle(self, request):
        if request == "Internet":
            print("With what you have problem ?")
            print(f"Client: {request}")
            return "I will fix it in minute"
        elif request == "computer":
            print("With what you have problem ?")
            print(f"Client: {request}")
            return "update your drivers"
        else:
            return super().handle(request)

class ManagerHandler(AbstractHandler):
    def handle(self, request):
        if request == "salary":
            print("why you call to me")
            print(f"\nClient: {request}")
            return "Oh ... We send your salary next week"
        else:
            print("why you call to me")
            print(request)
            return "I am busy"


def calling(handler,request):
    for i in request:
        result = handler.handle(i)
        if result:
            print(f"Phone: {result}", end="\n")
        else:
            print("Phone: bip bip bip ......", end="\n")


if __name__ == "__main__":

    itSpec = ITSpecialistHandler()
    callCentre = callCentreHandler()
    manager = ManagerHandler()
    answeringMachine = answeringMachineHandler()

    answeringMachine.set_next(callCentre).set_next(itSpec)
    calling(answeringMachine,["1","Yes","computer"])
    print("\n")


    print("lets try call call centre ")
    calling(callCentre,["1","Yes","Internet"])
    print("\n")

    answeringMachine.set_next(manager)
    calling(answeringMachine,["2","Salary"])
    print("\n")
