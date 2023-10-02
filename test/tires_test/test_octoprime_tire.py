import unittest
from tires.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def tire_should_be_serviced(self):
        array = [0.5, 0.9, 0.8, 0.9]
        tires = OctoprimeTire(array)
        self.assertTrue(tires.needs_service())

    def tire_should_not_be_serviced(self):
        array = [0.5, 0.5, 0.5, 0.5]
        tires = OctoprimeTire(array)
        self.assertFalse(tires.needs_service())


