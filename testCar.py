from Car import Car


# Start using the Class
car1 = Car('Toyota', 'White')
car1.displayCar()

car2 = Car('Tesla', 'Blue')
print(car2.label)
print(car2.color)

car3 = Car('Volvo', 'Black')
print(car3.label)
print(car3.color)

car3.color = 'Brown'
car3.displayCar()