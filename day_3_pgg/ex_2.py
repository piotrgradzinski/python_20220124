"""
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu 
elektrycznego. 
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może 
przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. 
Samochód powinien mieć także możliwość naładowania baterii.

https://yuml.me/preview/c83d768b

> car = ElectricCar(100)
> car.drive(70)
70
> car.drive(50)
30
> car.drive(50) 
0
> car.charge()
> car.drive(50)
50
"""

class ElectricCar:
    def __init__(self, max_range: int = 100) -> None:
        self.max_range = max_range
        self.battery_level = self.max_range

    def charge(self) -> None:
        self.battery_level = self.max_range

    def drive(self, distance: int) -> int:
        if distance <= self.battery_level:
            self.battery_level -= distance
            return distance
        else:
            tmp_bat = self.battery_level
            self.battery_level = 0
            return tmp_bat


car = ElectricCar(100)
print(car.drive(70))
print(car.drive(50))
print(car.drive(50))
car.charge()
print(car.drive(50))


car2 = ElectricCar(200)
print(car2.drive(250))

