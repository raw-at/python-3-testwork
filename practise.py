class Cars:
    #class variables hold by all the instances
    mileage = 12

    def  __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    @classmethod 
    def mileage_booster_fuel(cls,new_mileage):
        cls.mileage = new_mileage
    
    @staticmethod #method that doesn't have to do anything with the instance or the class itself

    def owner_name(name):
        print(name)
    

car_1 = Cars('Maruti Suzuki','Swift Dzire 2016',710000)
car_2 = Cars('Maruti Suzuki','Ciaz 2016',1110000)

print(car_1.brand,car_1.model)
print('Mileage',car_1.mileage); #getting class variable from instance

Cars.mileage_booster_fuel(15)
print('Mileage',car_1.mileage); 

Cars.owner_name('Bhopal Rawat')


car_1.mileage = 12.3
print('Mileage:',car_1.mileage)
print('Mileage:',car_2.mileage)




        