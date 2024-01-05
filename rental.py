class Rental:
    """Represents a rental of a car."""

    total = 0  # class variable    

    def __init__(self, customerId, carId, quantity, mode, startTime):
        """Initializes rental attributes."""
        Rental.total += 1
        self.id = Rental.total
        self.customerId = customerId
        self.carId = carId
        self.quantity = quantity
        self.mode = mode
        self.startTime = startTime
        self.endTime = None
        self.period = None
        self.totalCost = None

    def get_info(self):
        """Returns formatted rental info."""
        return f"rid={self.id} rmode={self.mode} qty={self.quantity} start={self.startTime} end={self.endTime} period={self.period} total={self.totalCost}"