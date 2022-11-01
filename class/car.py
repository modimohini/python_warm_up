class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.make} {self.odometer_reding}"
        return long_name.title()

my_new_car = Car('porsche', '718 Boxter', '2023')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reding = 89
use_car = my_new_car.get_descriptive_name()
print(use_car)