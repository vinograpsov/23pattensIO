from abc import ABC, abstractmethod
from datetime import datetime


class Game():
    _state = None
    def __init__(self, state) -> None:
        self._state = state
        print(f"My state is: {self._state}")
    def new_action(self, action) -> None:
        print("New action in game")
        self._state = action
        print(f"My state has changed to: {self._state}")
    def save(self):
        print("Game was saved")
        return ConcreteMemento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"My state has restored to: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())

    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._date} / ({self._state})"

    def get_date(self):
        return self._date


class Save_staker():
    def __init__(self, game):
        self._mementos = []
        self._game = game

    def make_backup(self) -> None:
        print("\nSaving state...")
        self._mementos.append(self._game.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print("Be careful all new changes will be delete")
        print(f"Restoring state to: {memento.get_name()}")
        self._game.restore(memento)


    def show_history(self) -> None:
        print("All your save points:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    civilisation6 = Game("New game")
    saves = Save_staker(civilisation6)
    saves.make_backup()

    civilisation6.new_action("destroy barbarians")
    saves.make_backup()

    civilisation6.new_action("make new city")
    saves.make_backup()

    civilisation6.new_action("make army")
    saves.make_backup()

    civilisation6.new_action("start new war")

    print("Oh no, i have so weak army, I will lose this war :( \n But ...... I have saves so lets restore my company :)")
    saves.show_history()

    saves.undo()

    saves.show_history()
