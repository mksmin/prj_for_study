class VehicleBase:
    def __init__(self, color):
        self.color = color

    def make_sound(self):
        print("No sound")

class Car(VehicleBase):
    def __init__(self, color, wheels):
        self.color = color
        # super().__init__(color)
        self.wheels = wheels

    def make_sound(self):
        print("Beep")

    def open_trunk(self):
        print('opened trunk')

class Ship(VehicleBase):
    def __init__(self, color, cabins):
        self.color = color
        self.cabins = cabins

    def make_sound(self):
        print("whooooo")

    def set_sail(self):
        print("set sail!")

class Amphibian(Car, Ship):
    def __init__(self, color, wheels):
        self.cabins = 0
        self.wheels = wheels
        self.color = color

    def toggle_mode(self):
        print("toggle mode")


car = Car('red', 4)
print(car.color, 'car with', car.wheels, 'wheels')

ship = Ship('blue', 2)
print(ship.color, 'ship with', ship.cabins, 'cabins')

amph = Amphibian('green', 4)
print(amph)
print(amph.__init__)
amph.make_sound()
print(amph.make_sound)


amph.open_trunk()
amph.set_sail()
