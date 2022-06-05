from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class Copy(Command):
    _command = "copied"

    def execute(self) -> None:
        print(self._command)

class Paste(Command):
    _command = "pasted"

    def execute(self) -> None:
        print(self._command)

class Save(Command):
    _command = "saved"

    def execute(self) -> None:
        print(self._command)



class Button:
    _executable_command = None

    def set_executable_command(self, command: Command):
        self._executable_command = command

    def onClick(self):
        print("Button click")
        self._executable_command.execute()


class ShortCut:
    _executable_command = None

    def set_executable_command(self, command: Command):
        self._executable_command = command

    def onUse(self):
        print("Shortcut used")
        self._executable_command.execute()


if __name__ == "__main__":
    copyShortcut = ShortCut()
    pasteShortcut = ShortCut()
    saveShortcut = ShortCut()

    copyButton = Button()
    pasteButton = Button()
    saveButton = Button()

    copyShortcut.set_executable_command(Copy())
    pasteShortcut.set_executable_command(Paste())
    saveShortcut.set_executable_command(Save())

    copyButton.set_executable_command(Copy())
    pasteButton.set_executable_command(Paste())
    saveButton.set_executable_command(Save())

    copyButton.onClick()
    copyShortcut.onUse()

    pasteButton.onClick()
    pasteShortcut.onUse()

    saveButton.onClick()
    saveShortcut.onUse()



