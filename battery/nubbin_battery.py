from battery.battery import Battery
from datetime import date
from dateutil.relativedelta import relativedelta


def NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().init(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        #return true if it has been more than 4 years since the last service date
        service_threshold_date = self.last_service_date + relativedelta(years=4)
        if service_threshold_date > datatime.today().date():
            return True
        else:
            return False


