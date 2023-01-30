# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 02:26:48 2023

@author: shiva
"""

# Program to illustrate factory design pattern.
# Here car is the factory with create car method deciding the type of the car.

class CarFactory:
    def create_car(self,car_type,*args,**kwargs):
        if car_type =="Sports":
            return SportsCar(*args,**kwargs)
        elif car_type == "SUV":
            return SUV(*args,**kwargs)


class SportsCar:
    def __init__(self,name,topspeed):
        self.name = name
        self.topspeed = topspeed
        

    def __str__(self):
        return f"{self.name} ({self.topspeed} km/hr)"
    
class SUV:
    def __init__(self,name,seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity
        
    def __str__(self):
        return f"{self.name} ({self.seating_capacity})"
    

factory = CarFactory()
sport_car = factory.create_car("Sports","Audi",35.5)
print(sport_car)