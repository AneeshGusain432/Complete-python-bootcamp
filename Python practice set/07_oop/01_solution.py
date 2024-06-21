class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_description():
        return "Cara are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricalCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
    

# my_tesla = ElectricalCar("Tesla", "Model S", "85KWH")


# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricalCar))

# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# My_car = Car("Tata", "Safari")
# Car("Tara", "Nexon")
# My_car.model = "Nisaan"

# print(My_car.model)
# print(My_car.general_description())
# print(Car.general_description())
# print(Car.total_car)
        
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = Car("Tata", "safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
        
    def engine_info(self):
        return "This is engine"

class ElectricalCarTwo(Battery, Engine, Car):
    pass

My_new_tesla = ElectricalCarTwo("Tesla", "Model S")
print(My_new_tesla.battery_info())
print(My_new_tesla.engine_info())



