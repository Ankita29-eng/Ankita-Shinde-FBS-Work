from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def calculate_toll(self):
        pass

class TwoWheeler(Vehicle):
    def __init__(self,persons):
        self.persons=persons

    def calculate_toll(self):
        basic = 20

        if self.persons > 2:
            extra_persons = self.persons - 2
            return basic + (extra_persons * 10)
        return basic

class ThreeWheeler(Vehicle):
    def __init__(self,persons):
        self.persons = persons

    def calculate_toll(self):
        basic = 30

        if self.persons > 3:
            extra_persons = self.persons - 3
            return basic + (extra_persons * 20)
        return basic

class FourWheeler(Vehicle):
    def __init__(self,persons):
        self.persons = persons

    def calculate_toll(self):
        basic = 40

        if self.persons > 4:
            extra_persons = self.persons - 4
            return basic +(extra_persons*40)
        return basic

class HeavyVehicle(Vehicle):
    def __init__(self,persons):
        self.persons = persons
    def calculate_toll(self):
        basic = 60

        if self.persons > 6:
            extra_persons = self.persons - 6
            return basic + (extra_persons* 100)
        return basic

def main():
    while True:
        print("\n--------TOLL CALCULATION-----------")
        print("1.Two Wheeler")
        print("2.Three Wheeler")
        print("3.Four Wheeler")
        print("4.Heavy Vehicle")
        print("5.Exit")

        choice = int (input("Enter your choice:"))
        if choice == 5:
            print("Thank you!")
            break
        persons = int(input("Enter number of persons:"))

        if choice == 1:
            Vehicle = TwoWheeler(persons)
        elif choice == 2:
            Vehicle = ThreeWheeler(persons)
        elif choice == 3:
            Vehicle = FourWheeler(persons)
        elif choice == 4:
            Vehicle = HeavyVehicle(persons)
        else:
            print("Invalid choice!")
            continue
        print("Total Toll = Rs.",Vehicle.calculate_toll())

main()
        