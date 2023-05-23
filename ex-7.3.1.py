class Temperature:
    def __init__(self, temp_cel, temp_fah):
        self.temp_cel = temp_cel
        self.temp_fah = temp_fah

    def get_input():
        return Temperature(
            float(input('Enter temperature in Celsius = ')),
            float(input('Enter temperature in Fahrenheit = '))
        )

    def cel_fah(self):
        fahrenheit = (self.temp_cel * 9/5) + 32
        return fahrenheit
    
    def fah_cel(self):
        celsius = (self.temp_fah - 32) * 5/9
        return celsius

    def display(self):
        print('Result:')
        print(self.temp_cel,'oC =', self.cel_fah(), 'oF')
        print(self.temp_fah,'oF =', self.fah_cel(), 'oC')

temp = Temperature.get_input()
temp.display()