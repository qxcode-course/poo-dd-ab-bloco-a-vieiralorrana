class Carro:
    def __init__(self, pas: int, km: int, passMax: int, gas: int, gasMax: int):
        self.pas = 0
        self.km = 0 
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
    
    def show(self):
        print(self)
    
    def __str__(self) -> str:
        return f"pass:{self.pas}, gas:{self.gas}, km:{self.km}"
    
    def enter(self):
        if self.pas < self.passMax:
            self.pas += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pas -= 1

    def fuel(self, increment: int):
        self.gas += increment
        if self.gas > self.gasMax:
            sobra: int = (self.gas - self.passMax)
            self.gas -= sobra
    
    def drive(self, distance: int):
        if 

    

def main():
    carro = Carro(0, 0, 2, 0, 100)

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        else:
            print("fail: comando desconhecido")




main()