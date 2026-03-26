import sys      
import csv      
import os       
import random  

class Cars:
    #This is the base class where most of the functions will be
    def __init__(self, make, model, year, owner_name):
        # e.g. Car("Ferrari", "F40", 1992, Dan Efoz)
        self.make = make
        self.model = model
        self.year = int(year)
        self.owner_name = owner_name

    def car_type(self):
        return "Car"
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} - {self.owner_name}"

class Sports_Car(Cars):
    # all sub classes of the base class Cars
    def __init__(self, make, model, year, owner_name, hp, top_speed):
        super().__init__(make, model, year, owner_name)
        self.hp = int(hp)
        self.top_speed = int(top_speed)

    def car_type(self):
        return "Sports" # will show the type of car displayed when requested to see the cars listed ad their info
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.hp}hp {self.top_speed}mph - {self.owner_name}"

class Super_Car(Cars):
    def __init__(self, make, model, year, owner_name, hp, top_speed, mode):
        super().__init__(make, model, year, owner_name)
        self.hp = int(hp)
        self.top_speed = int(top_speed)
        self.mode = mode

    def car_type(self):
        return "Super"

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.hp}hp {self.top_speed}mph {self.mode} - {self.owner_name}"

class Electric_Car(Cars):
    def __init__(self, make, model, year, owner_name, range):
        super().__init__(make, model, year, owner_name)
        self.range = int(range)

    def car_type(self):
        return "Electric"

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.range} - {self.owner_name}"

    

class Owner:
    # adding owner class to show who owns the specific car
    def __init__(self, name):
        self.name = name # e.g Dan Efoz
        self.cars = [] # list of cars that the owner owns
        if not name:
            raise ValueError("Owner name is missing")

    def add_car(self, car):
        if car not in self.cars: # makes sure cars aren't duplicated
            self.cars.append(car)

class Service_Record:
    # will represent any maintanance that needs to be added for the specific car
    def __init__(self, car_id, date, cost):
        self.car_id = car_id
        self.date = date
        self.cost = float(cost)

        
    

def display_menu():
    # when code is run this should be the first thing to come up
    print("Welcome to the Car Management System")
    choice = input("Choose what you like to do today")

        