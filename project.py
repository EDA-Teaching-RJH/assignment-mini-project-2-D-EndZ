import sys      
import csv      
import os       
import random  

class Cars:
    #This is the base class where most of the functions will be
    def __init__(self, make, model, year, owner):
        # e.g. Car("Ferrari", "F40", 1992, Ethan Hook)
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner

    make_list = [
    "Toyota",
    "Ford",
    "Honda",
    "BMW",
    "Audi",
    "Mercedes-Benz",
    "Tesla",
    "Nissan",
    "Volkswagen",
    "Porsche"
    "Lamborghini"
]
    model_list = [
    "Corolla",
    "Mustang GT",
    "Civic Type R",
    "M3 Competition",
    "A4 Quattro",
    "E63 AMG",
    "Model 3 Long Range",
    "GT-R R35",
    "Golf GTI",
    "911 Carrera"
    "Aventador SV"
]