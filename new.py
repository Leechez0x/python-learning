class Car:
    total_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_cars += 1

    def describe(self):
        return f"{self.year} {self.brand} {self.model}"

    @classmethod
    def from_string(cls, car_string):
        brand, model, year = car_string.split("-")
        return cls(brand, model, int(year))

    @staticmethod
    def is_valid_year(year):
        return 2000 <= year <= 2026


car1 = Car("Toyota", "Camry Spider", 2001)
car2 = Car("Mercedes", "Benz GLE 45", 2013)
car3 = Car.from_string("Honda-Civic-2019")

print(car1.describe())
print(car2.describe())
print(car3.describe())
print("Total cars created:", Car.total_cars)

print(Car.is_valid_year(2001))
print(Car.is_valid_year(1990))



class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery


    def sentence(self):
        return f"{self.brand} {self.model} has {self.battery}% battery"
    



phone1= Phone("iPhone", "11pro", 85)
phone2= Phone("Samsung", "S21", 72 )
phone3= Phone("Tecno", "Spark4", 12)

print(phone1.sentence())
print(phone2.sentence())
print(phone3.sentence())
print(phone3.battery + 10)