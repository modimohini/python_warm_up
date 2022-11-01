class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()

my_new_car = Car('porsche', '718 Boxter', '2023')
print(my_new_car.get_descriptive_name())