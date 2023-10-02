from datetime import datetime
from battery.battery import Battery

class SplinderBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.current_date + 3)
        if service_threshold_date > datatime.today().date():
            return True
        else:
            return False

