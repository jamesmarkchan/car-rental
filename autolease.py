from car import Car
from customer import Customer
from rental import Rental
import datetime as dt

class AutoLease:

    rental_rates = {
        "day": 35.00,  # USD
        "week": 220,
        "month": 980,
    }
    cars = [
        Car("Toyota", "Corolla", 2020, "blue", 1),
        Car("Ford", "Mustang", 2021, "green", 2),
        Car("Honda", "Civic", 2019, "red", 2),
        Car("Chevy", "Volt", 2016, "gray", 1)
    ]
    users = []
    rentals = []
    activeCustomer = None

    def run(self):
        """Runs the Auto Lease application."""
        print("Launching Auto Lease")

        # continuous while loop processes commands until user quits
        quit = False
        while quit == False:
            # query for action
            inputString = input("What would you like to do? ")
            inputString = inputString.lower()

            # check for quit
            if inputString == "quit" or inputString == "end" or inputString == "exit":
                quit = True
                print("Thank you for using the Auto Lease system")
                continue
            
            # process customer input
            print("Processing command: ", inputString)
            # print results
            if inputString == "rent" or inputString == "rental":
                # start a rental
                if self.activeCustomer == None:
                    print("Please select a customer first")
                    continue
                else :
                    print("Active customer is: ", self.activeCustomer.get_info())
                print("select car id to rent:")
                self.show_available_cars()
                carId = input("Car ID: ")
                quantity = input("Number of cars [1]: ")
                if quantity == "":
                    quantity = 1
                else:
                    quantity = int(quantity)
                if quantity < 0:
                    print("Number of cars must be greater than 0")
                    continue
                # get the car object from the card id
                car = self.cars[int(carId)-1]
                if car.quantity < quantity:
                    print("Not enough cars available")
                    continue
                mode = input("select mode to rent ([day]|week|month): ")
                if mode == "":
                    mode = "day"
                startTime = dt.datetime.now()
                newRental = Rental(self.activeCustomer.id, carId, quantity, mode, startTime)
                car.quantity -= quantity
                self.rentals.append(newRental)
            elif inputString == "return":
                # return a car
                email = input("Enter customer email: ")
                for user in self.users:
                    if user.email == email:
                        print("Found customer: ", user.get_info())
                        isActiveCustomer = input("Is this the active customer? ([yes]|no): ").lower()
                        if isActiveCustomer == "yes" or isActiveCustomer == "y" or isActiveCustomer == "":
                            self.activeCustomer = newCustomer
                            print("Active customer is: ", self.activeCustomer.get_info())
                        break

                # show the rental ids for the active customer
                print("Active customer rentals:")
                for rental in self.rentals:
                    if rental.customerId == self.activeCustomer.id:
                        print(rental.get_info())

                # select rental id to return
                rentalId = input("Enter rental id to return: ")
                for rental in self.rentals:
                    if rental.id == int(rentalId):
                        rental.endTime = dt.datetime.now()
                        rental.period = rental.endTime - rental.startTime
                        rental.totalCost = rental.period.days * self.rental_rates[rental.mode] * rental.quantity
                        car = self.cars[int(rental.carId)-1]
                        print("Rental returned:", rental.get_info())
                        print("Car:", car.get_descriptive_name())
                        print("Total cost:", "${:,.2f}".format(rental.totalCost))
                        car = self.cars[int(rental.carId)-1]
                        car.quantity += rental.quantity
                        break
            elif inputString == "list-cars" or inputString == "cars":
                # list all cars
                self.show_available_cars()
            elif inputString == "list-customers" or inputString == "customers":
                # list all customers
                self.list_customers()
            elif inputString == "new-customer" or inputString == "nc":
                # create new customer and option to set active customer
                name = input("Enter customer full name: ")
                email = input("Enter customer email: ")
                phone = input("Enter customer phonenumber: ")
                newCustomer = Customer(name, email, phone)
                self.users.append(newCustomer)
                isActiveCustomer = input("Is this the active customer? ([yes]|no): ").lower()
                if isActiveCustomer == "yes" or isActiveCustomer == "y" or isActiveCustomer == "":
                    self.activeCustomer = newCustomer
                    print("Active customer is: ", self.activeCustomer.get_info())
            elif inputString == "find-customer" or inputString == "find":
                # find customer by email and option to set active customer
                print("Enter customer email: ")
                email = input("Email: ")
                for user in self.users:
                    if user.email == email:
                        print("Found customer: ", user.get_info())
                        isActiveCustomer = input("Is this the active customer? ([yes]|no): ").lower()
                        if isActiveCustomer == "yes" or isActiveCustomer == "y" or isActiveCustomer == "":
                            self.activeCustomer = newCustomer
                            print("Active customer is: ", self.activeCustomer.get_info())
                        break
            elif inputString == "select-customer" or inputString == "sc":
                # select customer by id
                print("select customer id:")
                self.list_customers()
                customerId = input("Customer ID: ")
                self.activeCustomer = self.users[int(customerId)-1]
                print("Active customer is: ", self.activeCustomer.get_info())
            elif inputString == "active-customer" or inputString == "ac":
                # show active customer
                print("Active customer is: ", self.activeCustomer.get_info())
            elif inputString == "list-rentals" or inputString == "rentals" or inputString == "lr":
                # list all rentals
                self.list_rentals()
            elif inputString == "help" or inputString == "h":
                # show help
                print("Commands:")
                print("quit - quit the program")
                print("rent - start a rental")
                print("return - return a rental")
                print("list-cars - list all available cars")
                print("list-customers - list all customers")
                print("new-customer - create a new customer")
                print("find-customer - find a customer by email")
                print("select-customer - select a customer by id")
                print("active-customer - show the active customer")
                print("list-rentals - list all rentals")
                print("help - show this help")
            else:
                print("Unknown command:", inputString)
        else:
            # quit by exiting the while loop
            print("Exiting Auto Lease")

    def show_available_cars(self):
        """Show available vehicals to rent."""
        print("Available vehicles are:")
        for car in self.cars:
            print(car.get_info_with_quantity())

    def list_customers(self):
        """List all customers."""
        print("All customers:")
        for user in self.users:
            print(user.get_info())

    def list_rentals(self):
        """List all rentals."""
        print("All rentals:")
        for rental in self.rentals:
            print(rental.get_info())
            car = self.cars[int(rental.carId)-1]
            customer = self.users[int(rental.customerId)-1]
            print("Car:", car.get_descriptive_name())
            print("Customer:", customer.get_info())
            print("")


def main():
    app = AutoLease()
    app.run()


if __name__ == "__main__":
    main()