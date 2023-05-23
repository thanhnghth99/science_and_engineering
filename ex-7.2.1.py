# Define the Class Car
class Car:
    def __init__(self, label, color):
        self.label = label
        self.color = color

    def displayCar(self):
        print(self.label)
        print(self.color)

# Start using the Class
car1 = Car('Toyota', 'White')
car1.displayCar()

car2 = Car('Tesla', 'Blue')
print(car2.label)
print(car2.color)

car3 = Car('Volvo', 'Black')
print(car3.label)
print(car3.color)

car3.color = 'Gray'
car3.displayCar()