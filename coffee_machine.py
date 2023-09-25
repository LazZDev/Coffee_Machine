class CoffeeMachine:
    def __init__(self, water, coffee_beans, milk, cups):
        self.water = water
        self.coffee_beans = coffee_beans
        self.milk = milk
        self.cups = cups

    def check_resources(self, water_needed, coffee_needed, milk_needed, cups_needed):
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
        resources_status = self.check_resources(water_needed, coffee_needed, milk_needed, cups_needed)
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
        self.water += water_added
        self.coffee_beans += coffee_added
        self.milk += milk_added
        self.cups += cups_added
        print("Refilled resources.")

    def check_status(self):
        print(f"Water: {self.water}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Milk: {self.milk}ml")
        print(f"Cups: {self.cups}")

# Instantiate a CoffeeMachine object with initial resources
coffee_machine = CoffeeMachine(water=1000, coffee_beans=200, milk=500, cups=10)

while True:
    action = input("What would you like to do? (buy/fill/take/remaining/exit): ")

    if action == "buy":
        choice = input("What type of coffee would you like? (1: Espresso, 2: Latte, 3: Cappuccino, back: Go back): ")
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
        water = int(input("Enter the amount of water to add (ml): "))
        coffee_beans = int(input("Enter the amount of coffee beans to add (g): "))
        milk = int(input("Enter the amount of milk to add (ml): "))
        cups = int(input("Enter the number of cups to add: "))
        coffee_machine.fill_resources(water, coffee_beans, milk, cups)
    elif action == "take":
        print(f"Taking ${coffee_machine.make_coffee(0, 0, 0, 0, 0)} from the machine.")
    elif action == "remaining":
        coffee_machine.check_status()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")
