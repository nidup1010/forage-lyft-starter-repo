import unittest
from tires.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def tire_should_be_serviced(self):
        array = [0.2, 0.9, 0.8, 0.2]
        tires = CarriganTire(array)
        self.assertTrue(tires.needs_service())

    def tire_should_not_be_serviced(self):
        array = [0.2, 0.7, 0.8, 0.1]
        tires = CarriganTire(array)
        self.assertFalse(tires.needs_services())

