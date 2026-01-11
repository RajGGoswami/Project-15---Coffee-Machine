# Project-15---Coffee-Machine

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to simulate a coffee machine system that manages resources, processes payments, and serves drinks based on user input.

**Project Overview**

The Coffee Machine allows the user to:

Choose a coffee type

Insert coins to pay

Receive change if overpaid

View current machine resources

Turn the machine off

Available drinks:

Espresso

Latte

Cappuccino

**Project File Structure**

main.py
Contains the coffee machine logic, user interaction, and transaction flow.

menu.py
Stores the coffee menu, ingredient requirements, and machine resources.

art.py
Contains ASCII art for the coffee machine logo.

**Why this project exists**

This project helped me understand how to model a real-world system using code.

It required combining logic, data structures, and state management in a way that closely resembles how actual machines work.

**What I learned**

How to work with nested dictionaries

How to validate resource availability

How to simulate financial transactions

How to manage shared state across functions

How to break a large problem into smaller reusable functions

How to design user-driven program flow

**How the code works (step-by-step)**

Display the coffee machine logo

Prompt the user for a drink selection

Allow special commands like report and off

Check if sufficient ingredients are available

Ask the user to insert coins

Validate the transaction and calculate change

Deduct ingredients and serve the coffee

Repeat until the machine is turned off

**Example Output**

What would you like? (espresso/latte/cappuccino):
latte

Please insert coins

How many quarters?:
10

Here is your latte ☕ Enjoy!
