class Customer:
    """Represents a rental car."""

    total = 0  # class variable

    def __init__(self, name, email, phone=""):
        """Initializes customer attributes."""
        self.name = name
        self.email = email
        self.phone = phone
        Customer.total += 1
        self.id = Customer.total
        
    def get_info(self):
        """Returns a neatly formatted customer info."""
        customer_info = f"{self.id} {self.name.title()} {self.email} {self.phone}"
        return customer_info