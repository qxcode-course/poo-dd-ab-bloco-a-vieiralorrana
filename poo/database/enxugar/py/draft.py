class Towel:
    def __init__(self, color: str, size: str, wetness: int):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0 
    
    def show(self) -> None:
        print(self); 
    
    def __str__(self) -> str:
        return f"Cor: {self.color}, Tam: {self.size}, Umidade: {self.wetness}"
    
    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10;
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30;
        return 0
    
    def dry(self, amount: int) -> None: 
        self.wetness += amount;
        if self.wetness > self.getMaxWetness():
            print("toalha enchardada")
        self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetnesss = 0
    
    def isDry(self) -> bool:
        return self.wetness == 0;



def main():
    toalha = Towel("", "", 0)

    while True:
        print("$", end="")
        line: str = input()
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break;
        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size, 0)
        elif args[0] == "mostrar":
            print(toalha)
        elif args[0] == "enxugar":
            amount = int(args[1])
            toalha.dry(amount);
        elif args[0] == "trocer":
            return toalha.wetness == 0
        else:
            print("fail: comando desconhecido")


main()