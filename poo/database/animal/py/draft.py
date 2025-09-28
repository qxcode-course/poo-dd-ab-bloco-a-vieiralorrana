class Animal:
    def __init__(self, species: str, age: int, sound: str):
        self.species = species
        self.age = 0
        self.sound = sound

    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
    
    def ageBy(self, increment: int):
        self.age += increment
        if self.age >=  4:
            print(f"warning: {self.species} morreu")
            self.age = 4

    def makeSound(self):
        if self.age == 0:
            return "---"
        elif self.age == 4:
            return "RIP"
        else:
            return self.sound
        
def main():
    animal = Animal("", 0, "")

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, 0, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "grow":
            increment = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            print(animal.makeSound())
        else:
            print("fail: comando desconhecido")
        



main()