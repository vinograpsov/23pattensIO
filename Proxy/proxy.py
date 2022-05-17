from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def payment(self, count):
        pass

class Money(Payment):
    def __init__(self,count):
        self.count = count

    def payment(self, count):
        if self.count > count:
            self.count -= count
            print(f"Paid by cash {count}")
        else:
            print("no money :(")

class Credit_card(Payment):
    def __init__(self, money):
        self._money = money

    def payment(self, count):
        if self._money.count > count:
            self._money.count -= count
            print(f"paid by credit card {count}")
        else:
            print("no money :(")

    def put_money(self, count):
        if self._money.count > count:
            self._money.count += count
        else:
            print("no money :(")
if __name__ == "__main__":
    cash = Money(100)

    cash.payment(50)
    cash.payment(60)

    creditCard = Credit_card(cash)

    creditCard.put_money(40)
    creditCard.put_money(50)

    creditCard.payment(30)
    creditCard.payment(1030)
