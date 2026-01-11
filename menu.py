# Menu and resource configuration for the Coffee Machine
#
# This file acts as a data source for the main program.
# It contains:
# - Available coffee options
# - Ingredient requirements for each drink
# - Cost of each drink
# - Initial machine resource levels


# MENU dictionary stores all coffee options and their requirements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,     # ml of water required
            "coffee": 18,    # grams of coffee required
        },
        "cost": 1.5,        # price in dollars
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# resources dictionary represents the machine’s current stock
resources = {
    "water": 300,    # ml
    "milk": 200,     # ml
    "coffee": 100,   # grams
    "money": 0,      # dollars earned
}
