class Calculadora:
    def __init__(self, battery: int, display: int, batteryMax: int):
        self.battery = 0
        self.display = 0
        self.batteryMax = batteryMax

    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, increment: int):
        if self.battery < self.batteryMax:
            self.battery += increment
            if self.battery > self.batteryMax:
                self.battery = self.batteryMax
        else:
            print("bateria cheia")

    
    def soma(self, a: int, b: int):
        if self.battery > 0:
            self.display = (a + b)
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")

    def divisao(self, a: int, b: int):
        if self.battery > 0:
            if b == 0:
                print("fail: divisao por zero")
            else:
                self.display = (a / b)
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")
        

def main():
    calculadora = Calculadora(0, 0, 0)

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora = Calculadora(0, 0, batteryMax)
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            increment = int(args[1])
            calculadora.charge(increment)
        elif args[0] == "sum":
            a = int(args[1])
            b = int(args[2])
            calculadora.soma(a, b)
        elif args[0] == "div":
            a = int(args[1])
            b = int(args[2])
            calculadora.divisao(a, b)
        else:
            print("fail: comando desconhecido")

main()