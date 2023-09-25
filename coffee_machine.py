class CoffeeMachine:
    def __init__(self, water, coffee_beans, milk, cups):
        # Initialize the coffee machine with the specified amounts of water, coffee beans, milk, and cups
        self.water = water
        self.coffee_beans = coffee_beans
        self.milk = milk
        self.cups = cups

    def check_resources(self, water_needed, coffee_needed, milk_needed, cups_needed):
        # Check if the coffee machine has enough resources to make a coffee order with the specified amounts of water, coffee beans, milk, and cups
        if self.water < water_needed:
            return "Sorry, not enough water."
        elif self.coffee_beans < coffee_needed:
            return "Sorry, not enough coffee beans."
        elif self.milk < milk_needed:
            return "Sorry, not enough milk."
        elif self.cups < cups_needed:
            return "Sorry, not enough cups."
        else:
            return "OK"

    def make_coffee(self, water_needed, coffee_needed, milk_needed, cups_needed, cost):
        # Make a coffee order with the specified amounts of water, coffee beans, milk, and cups, and return the cost of the coffee
        resources_status = self.check_resources(
            water_needed, coffee_needed, milk_needed, cups_needed)
        if resources_status == "OK":
            print("Making coffee...")
            self.water -= water_needed
            self.coffee_beans -= coffee_needed
            self.milk -= milk_needed
            self.cups -= cups_needed
            return cost
        else:
            return resources_status

    def fill_resources(self, water_added, coffee_added, milk_added, cups_added):
        # Add the specified amounts of water, coffee beans, milk, and cups to the coffee machine's resources
        self.water += water_added
        self.coffee_beans += coffee_added
        self.milk += milk_added
        self.cups += cups_added
        print("Refilled resources.")

    def check_status(self):
        # Print out the current status of the coffee machine, including the amount of water, coffee beans, milk, and cups
        print(f"Water: {self.water}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Milk: {self.milk}ml")
        print(f"Cups: {self.cups}")


# Instantiate a CoffeeMachine object with initial resources
coffee_machine = CoffeeMachine(water=1000, coffee_beans=200, milk=500, cups=10)

while True:
    action = input(
        "What would you like to do? (buy/fill/take/remaining/exit): ")

    if action == "buy":
        # Prompt the user to choose a type of coffee, and make the coffee order with the appropriate amounts of resources
        choice = input(
            "What type of coffee would you like? (1: Espresso, 2: Latte, 3: Cappuccino, back: Go back): ")
        if choice == "1":
            cost = coffee_machine.make_coffee(250, 16, 0, 1, 4)
        elif choice == "2":
            cost = coffee_machine.make_coffee(350, 20, 75, 1, 7)
        elif choice == "3":
            cost = coffee_machine.make_coffee(200, 12, 100, 1, 6)
        elif choice == "back":
            continue
        else:
            print("Invalid choice.")
            continue

        if cost:
            print(f"Enjoy your coffee! That'll be ${cost}")
    elif action == "fill":
        # Prompt the user to enter the amounts of resources to add, and add them to the coffee machine's resources
        water = int(input("Enter the amount of water to add (ml): "))
        coffee_beans = int(
            input("Enter the amount of coffee beans to add (g): "))
        milk = int(input("Enter the amount of milk to add (ml): "))
        cups = int(input("Enter the number of cups to add: "))
        coffee_machine.fill_resources(water, coffee_beans, milk, cups)
    elif action == "take":
        # Simulate taking money from the coffee machine by making a coffee order with zero resources
        print(
            f"Taking ${coffee_machine.make_coffee(0, 0, 0, 0, 0)} from the machine.")
    elif action == "remaining":
        # Print out the current status of the coffee machine
        coffee_machine.check_status()
    elif action == "exit":
        # Exit the program
        break
    else:
        print("Invalid action. Please try again.")
