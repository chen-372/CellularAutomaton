class Home:
    height = 3
    x_len = 10
    y_len = 10

    def __init__(self, name: str) -> None:
        self.owner = name
        self.pet = []

    def add_pet(self, name: str) -> None:
        self.pet.append(name)

    @staticmethod
    def adder(n1: int, n2: int) -> int:
        return n1 + n2

    def __str__(self) -> str:
        return f"owner: {self.owner} pet: {self.pet}"

    def __repr__(self) -> str:
        return f"owner: {self.owner} pet: {self.pet}"


homes = [Home("Cris"), Home("Charles")]

for h in homes:
    print(h)
print(homes)

# print(home1.pet)
# print(home1.owner)

# print(home2.pet)
# print(home2.owner)
