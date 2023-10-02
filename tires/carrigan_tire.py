from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, array):
        self.array = array

    def needs_service(self):
        for value in self.array:
            if value >= 0.9:
                return True
        return False

