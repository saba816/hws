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
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print('The vehicle is now charged.')

    def fuel_up(self):
        print('This vehicle has no fuel tank!')

import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(brand="Toyota", model="Camry", type="Sedan")

    def test_fuel_up(self):
        self.vehicle.fuel_up()
        self.assertEqual(self.vehicle.fuel_level, self.vehicle.gas_tank_size)

    def test_drive(self):
        expected_output = f'The {self.vehicle.model} is now driving.'
        with self.assertLogs(level='INFO') as logs:
            self.vehicle.drive()
            self.assertEqual(logs.output, [f'INFO:root:{expected_output}'])

class TestElectricVehicle(unittest.TestCase):
    def setUp(self):
        self.electric_vehicle = ElectricVehicle(brand="Tesla", model="Model S", type="Electric")

    def test_charge(self):
        self.electric_vehicle.charge()
        self.assertEqual(self.electric_vehicle.charge_level, 100)

    def test_fuel_up(self):
        expected_output = 'This vehicle has no fuel tank!'
        with self.assertLogs(level='INFO') as logs:
            self.electric_vehicle.fuel_up()
            self.assertEqual(logs.output, [f'INFO:root:{expected_output}'])

if __name__ == '__main__':
    unittest.main()
