import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_service(self):
        current_date = datetime.today().date()
        last_service_date = today.replace(year=current_date.year - 5)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = today.replace(year=current_date.year - 3)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

