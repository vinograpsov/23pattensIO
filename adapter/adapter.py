class Memory:
    def request(self, number: str):
        return number


class User:
    def user_request(self, number):
        return number


class Adapter(Memory, User):
    def request(self, number):
        return bin(self.user_request(number))

if __name__ == "__main__":
    print("I can work just fine with binary numbers:")
    memory = Memory()
    print(f"I was reruested command {memory.request('0b101')} \n")

    user_nums = User()
    print("I dont understand numbers entered by user")
    print(f"command send {user_nums.user_request(5)} \n")

    print("We can make it understandable to me, due to adapter")
    adapter = Adapter()
    print(f"Translated to binary {adapter.request(5)}")