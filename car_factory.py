#this class should create all the cars
from car import Car
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine 
from engine.willoughby_engine import WilloughbyEngine 

from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery



class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date,warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
