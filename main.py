# Day 15 – Coffee Machine
# Part of my 100 Days of Code journey
#
# This program simulates a real-world coffee machine.
# It manages resources, takes user input, processes payments,
# and serves coffee until the machine is turned off.

from menu import MENU, resources   # Import menu options and machine resources
from art import logo               # Import ASCII logo for visual feedback


def display_report(item):
    """
    Displays the current state of machine resources.
    This function is triggered when the user types 'report'.
    """
    print(
        f"Water: {item['water']}ml\n"
        f"Milk: {item['milk']}ml\n"
        f"Coffee: {item['coffee']}g\n"
        f"Money: ${item['money']}"
    )


def sufficient_resource(user_coffee):
    """
    Checks whether the machine has enough ingredients
    to make the selected coffee.

    Loops through each required ingredient and compares it
    with available resources.

    Returns:
        True  -> if all ingredients are sufficient
        False -> if any ingredient is insufficient
    """
    for key in user_coffee['ingredients']:
        if resources[key] < user_coffee['ingredients'][key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def check_transaction(cash_inserted, coffee_cost):
    """
    Validates whether the user has inserted enough money.

    If insufficient money is provided:
        - Transaction fails

    If extra money is provided:
        - Calculates and returns change

    Returns:
        True  -> transaction successful
        False -> transaction failed
    """
    if coffee_cost > cash_inserted:
        return False
    elif coffee_cost < cash_inserted:
        money_change = round((cash_inserted - coffee_cost), 2)
        print(f"Here is ${money_change} in change.")
        return True
    else:
        # Exact payment
        return True


def process_coins():
    """
    Asks the user how many coins they are inserting.
    Converts coin count into a total monetary value.

    Returns:
        Total amount of money inserted by the user
    """
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def make_coffee(coffee_ingredients):
    """
    Deducts the required ingredients from the machine's
    available resources after a successful purchase.
    """
    for key in coffee_ingredients:
        resources[key] -= coffee_ingredients[key]


# Flag to keep the coffee machine running
machine_on = True

# Display the coffee machine logo when the program starts
print(logo)

# Main program loop – runs until the machine is turned off
while machine_on:

    # Ask user what they want to do
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    # Turn off the machine
    if user_choice == "off":
        machine_on = False

    # Print current resource report
    elif user_choice == "report":
        display_report(resources)

    # Handle coffee order
    else:
        coffee = MENU[user_choice]

        # Check if enough ingredients exist
        if sufficient_resource(coffee):
            print("Please insert coins")

            # Process inserted coins
            user_money = round(process_coins(), 2)

            # Validate transaction
            if check_transaction(user_money, coffee['cost']):
                # Add money to machine
                resources['money'] += coffee['cost']

                # Deduct ingredients
                make_coffee(coffee['ingredients'])

                # Serve coffee
                print(f"Here is your {user_choice} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")
