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