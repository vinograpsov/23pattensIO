from abc import ABC, abstractmethod

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class Number(AbstractExpression):
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class Add(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"

class Subtract(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"

class Multiply(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

    def __repr__(self):
        return f"({self.left} Multiply {self.right})"

class Devide(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

    def __repr__(self):
        return f"({self.left} Devide {self.right})"


if __name__ == "__main__":
    sentence = "9 + 5 - 2 * 3 / 2"
    print(sentence)
    tokens = sentence.split(" ")
    print(tokens)
    examples = []
    examples.append(Add(Number(tokens[0]), Number(tokens[2])))
    examples.append(Subtract(examples[0], Number(tokens[4])))
    examples.append(Multiply(examples[1], Number(tokens[6])))
    examples.append(Devide(examples[2], Number(tokens[8])))
    print(examples)
    print(examples[-1].interpret())
    print(examples[-1])