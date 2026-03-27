from project import Cars, valid_plate

def test_plate_valid():
    assert valid_plate("AB12 XYZ")
    assert not valid_plate("A123 XYZ")
    assert not valid_plate("AB12XYZ")