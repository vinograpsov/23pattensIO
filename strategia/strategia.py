from abc import ABC, abstractmethod
class Typing():
    def __init__(self, strategy):
        self._strategy = strategy

    def strategy(self, strategy):
        self._strategy = strategy


    def print_line_with_strategy(self,new_line):
        print(self._strategy.type(new_line))

class TypingSort(ABC):
    @abstractmethod
    def type(self, data):
        pass


class NormalType(TypingSort):
    def type(self, data):
        return data


class ReversedType(TypingSort):
    def type(self, data):
        return list(reversed(data))

class UppercaseType(TypingSort):
    def type(self, data):
        for i in range(len(data)):
            data[i] = data[i].upper()
        return data

class LowcaseType(TypingSort):
    def type(self, data):
        for i in range(len(data)):
            data[i] = data[i].lower()
        return data

if __name__ == "__main__":
    typing = Typing(NormalType())
    typing.print_line_with_strategy(['A','b','c','D','e'])

    typing.strategy(LowcaseType())
    typing.print_line_with_strategy(['A','b','c','D','e'])

    typing.strategy(UppercaseType())
    typing.print_line_with_strategy(['A','b','c','D','e'])

    typing.strategy(ReversedType())
    typing.print_line_with_strategy(['A','b','c','D','e'])


    print()