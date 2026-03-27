import sys      
import csv      
import os       
import random  
import cowsay
import re

class Cars:
    #This is the base class where most of the functions will be
    def __init__(self, make, model, year, plate, owner_name):
        # e.g. Car("Ferrari", "F40", 1992, Dan Efoz)
        self.make = make
        self.model = model
        self.year = int(year)
        self.owner_name = owner_name
        self.plate = plate

    def car_type(self):
        return "Car"
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} - {self.owner_name}"

class Sports_Car(Cars):
    # all sub classes of the base class Cars
    def __init__(self, make, model, year, plate, owner_name, hp, top_speed):
        super().__init__(make, model, year, plate, owner_name)
        self.hp = int(hp)
        self.top_speed = int(top_speed)

    def car_type(self):
        return "Sports" # will show the type of car displayed when requested to see the cars listed ad their info
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.hp}hp {self.top_speed}mph - {self.owner_name}"

class Super_Car(Cars):
    def __init__(self, make, model, year, plate, owner_name, hp, top_speed, mode):
        super().__init__(make, model, year, plate, owner_name)
        self.hp = int(hp)
        self.top_speed = int(top_speed)
        self.mode = mode

    def car_type(self):
        return "Super"

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.hp}HP {self.top_speed}mph {self.mode} - {self.owner_name}"

class Electric_Car(Cars):
    def __init__(self, make, model, year, plate, owner_name, range):
        super().__init__(make, model, year, plate, owner_name)
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

    def __str__(self):
        return f"{self.name}"

class Service_Record:
    # will represent any maintanance that needs to be added for the specific car
    def __init__(self, car_id, date, cost):
        self.car_id = car_id
        self.date = date
        self.cost = float(cost)

    def __str__(self):
        return f"{self.date}:x (£{self.cost})"

        
def setup_files_csv():
    # creates a new file called cars.csv/ servives.csv, opens it in write mode, creates a csv writer, then writes the header rows listed down below
    if not os.path.exists("cars.csv"):
        with open("cars.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Type", "Make", "Model", "Year", "Plate", "Owner_Name",
                         "Range", "HP", "TopSpeed", "Mode"])

    if not os.path.exists("services.csv"):
        with open("services.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["CarID", "Date", "Cost"])

def load_cars():
    #will load all the cars from the csv file into objects
    cars = []
    with open("cars.csv", "r") as f:
        reader = csv.reader(f)
        next(reader) # will skip the header row
        for row in reader:
            car_type = row[0]
            make = row[1]
            model = row[2]
            year = row[3]
            plate = row[4]
            owner = row[5] 

            # these might be empty depending on the car type
            range = row[6] if row[6] != "" else 0 # allows it to run even if the value is empty
            hp = row[7] if row[7] != "" else 0
            top_speed = row[8] if row[8] != "" else 0
            mode = row[9]
            # made changes to this because the other way kept crashing due to hp being empty because of the way i wrote the csv file

            if car_type == "Electric":
                car = Electric_Car(make, model, year, plate, owner, range) # eg electric car only has range as extra 
            elif car_type == "Sports":
                car = Sports_Car(make, model, year, plate, owner, hp, top_speed)
            elif car_type == "Super":
                car = Super_Car(make, model, year, plate, owner, hp, top_speed, mode)
            else:
                car = Cars(make, model, year, plate, owner)
            cars.append(car)
    return cars

def save_car(car):
    # saves one car object to the csv file
    car_type = car.car_type()

    with open("cars.csv", "a", newline="") as f:
        w = csv.writer(f)

        if car_type == "Electric":
            w.writerow(["Electric", car.make, car.model, car.year, car.plate, car.owner_name,
                        car.range, "", "", ""])

        elif car_type == "Sports":
            w.writerow(["Sports", car.make, car.model, car.year, car.plate, car.owner_name,
                        "", car.hp, car.top_speed, ""])

        elif car_type == "Super":
            w.writerow(["Super", car.make, car.model, car.year, car.plate, car.owner_name,
                        "", car.hp, car.top_speed, car.mode])

        else:
            # basic car
            w.writerow(["Car", car.make, car.model, car.year, car.plate, car.owner_name,
                        "", "", "", ""])

def load_services():
    services = []
    with open("services.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            services.append(row)
    return services    

def save_service(car_id, date, cost):
    with open("services.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([car_id, date, cost])

def valid_plate(plate):
    pattern = r"^[A-Z]{2}[0-9]{2} [A-Z]{3}$"
    return re.match(pattern, plate) is not None

def add_car():
    print("\nAdd Your Car")
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    owner = input("Owner: ")

    plate = input("Enter your license plate (AB12 XYZ)").upper()
    if not valid_plate(plate): # uses the reg ex rules to check if the license plate is valid
        print("License Plate not valid")
        return
    
    #pretty self explanitory i think
    print("1.Standard\n2.Sports\n3.Super\n4.Electric")
    t = input("Type: ")
    if t == "2":
        hp = input("Horsepower: ")
        top_speed = input("Top Speed: ")
        car = Sports_Car(make, model, year, plate, owner, hp, top_speed)
    elif t == "3":
        hp = input("Horsepower: ")
        top_speed = input("Top Speed: ")
        mode = input("What mode has it got: ")
        car = Super_Car(make, model, year, plate, owner, hp, top_speed, mode)
    elif t == "4":
        range = input("Range in miles: ")
        car = Electric_Car(make, model, year, plate, owner, range)
    else:
        car = Cars(make, model, year, plate, owner)

    save_car(car)
    cowsay.cow("Car added!") #added use of external libraries

def list_cars():
    print("\nCars:")
    cars = load_cars()

    if not cars:
        print("No cars.")
        return

    i = 1   # manual counter
    for c in cars:
        print(f"{i}. {c}")
        i += 1

def add_service_record():
    print("\nAdd Service Record")

    cars = load_cars()
    if not cars:
        print("No cars available.")
        return

    # show cars so the user knows which one to pick
    print("\nSelect a car:")
    i = 1
    for c in cars:
        print(f"{i}. {c}")
        i += 1

    car_id = input("Enter car number: ")

    date = input("Service date (YYYY-MM-DD): ")
    cost = input("Service cost: ")

    save_service(car_id, date, cost)
    print("Service record saved.")

def list_services():
    print("\nService Records:")
    services = load_services()
    cars = load_cars()
    if not services:
        print("No service records.")
        return
    
    index = 1  # manual counter 

    for s in services:
        car_index = int(s[0]) - 1  # convert car number to list index
        if 0 <= car_index < len(cars):
            # print service with car info
            print(f"{index}. {cars[car_index]} -> Date: {s[1]}, Cost: £{s[2]}")

        index += 1

def main():
    setup_files_csv()
    # when code is run  this should be the first thing to come up
    while True:
        print("Welcome to the Car Management System")
        print("1. Add Car")
        print("2. List Cars")
        print("3. Add Service Record")
        print("4. List Service Records")
        print("5. Exit")

        choice = input("Choose what you like to do today ")

        if choice == "1":
            add_car()
        elif choice == "2":
            list_cars()
        elif choice == "3":
            add_service_record()
        elif choice == "4":
            list_services()
        elif choice == "5":
            print("Later g ...")
            break
        else:
            print("Invalid Option g")

if __name__ == "__main__":
    main()

        