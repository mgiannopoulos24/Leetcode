class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Initialize the number of available slots for each car type
        self.slots = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # Check if there's an available slot for the given car type
        if self.slots[carType] > 0:
            self.slots[carType] -= 1  # Park the car, reduce the available slots
            return True
        return False  # No available slot


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)