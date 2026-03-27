# importing the stuff i  want to test from the main project file
from project import Cars, valid_plate, Sports_Car, Super_Car, Electric_Car

def test_plate_valid():
    assert valid_plate("AB12 XYZ")
    assert not valid_plate("A123 XYZ")
    assert not valid_plate("AB12XYZ")

def test_sports_car_str():
    car = Sports_Car("Ferrari", "488", 2018, "LP21 EFO", "Dan Efoz", 788, 210 )
    assert str(car) == "Ferrari 488 2018 660hp 205mph - Dan"

def test_super_car_str():
    car = Super_Car("Lamborghini", "Aventador", 2020, "AB12 XYZ", "Efoz", 740, 217, "Track")
    assert str(car) == "Lamborghini Aventador 2020 740HP 217mph Track - Efoz"

def test_electric_car_str():
    car = Electric_Car("Tesla", "Model 3", 2022, "AB12 XYZ", "Bob", 300)
    assert str(car) == "Tesla Model 3 2022 300 - Bob"