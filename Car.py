# Define the Class Car
class Car:
    def __init__(self, label, color):
        self.label = label
        self.color = color

    def displayCar(self):
        print(self.label)
        print(self.color)