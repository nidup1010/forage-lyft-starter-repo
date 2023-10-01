from battery import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        #return true if it has been more than 4 years since the last service date
        # service_threshold_date = self.last_service_date + relativedelta(years=4)
        service_threshold_date = self.last_service_date.replace(year=self.current_date + 4)
        if service_threshold_date > datatime.today().date():
            return True
        else:
            return False


