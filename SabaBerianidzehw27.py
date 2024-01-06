#1

class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        return 'Gas tank is now full.'

    def drive(self):
        return f'The {self.model} is now driving.'


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        return 'The vehicle is now charged.'

    def fuel_up(self):
        return 'This vehicle has no fuel tank!'

import pytest

@pytest.fixture
def vehicle_instance():
    return Vehicle(brand="Toyota", model="Camry", type="Sedan")

@pytest.fixture
def electric_vehicle_instance():
    return ElectricVehicle(brand="Tesla", model="Model S", type="Electric")

def test_vehicle_fuel_up(vehicle_instance):
    vehicle_instance.fuel_up()
    assert vehicle_instance.fuel_level == vehicle_instance.gas_tank_size

def test_vehicle_drive(vehicle_instance, capsys):
    vehicle_instance.drive()
    captured = capsys.readouterr()
    expected_output = f'The {vehicle_instance.model} is now driving.\n'
    assert captured.out == expected_output

def test_electric_vehicle_charge(electric_vehicle_instance):
    electric_vehicle_instance.charge()
    assert electric_vehicle_instance.charge_level == 100

def test_electric_vehicle_fuel_up(electric_vehicle_instance, capsys):
    electric_vehicle_instance.fuel_up()
    captured = capsys.readouterr()
    expected_output = 'This vehicle has no fuel tank!\n'
    assert captured.out == expected_output
