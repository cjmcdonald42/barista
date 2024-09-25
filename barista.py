#
#       project: barista.py
#        author: Charles J McDonald <cmcdonald@woonsocketschools.com>
#  last updated: 09/23/2024
#
#   description: Meet Cuppa Joe, the robot barista
#       version: 1.0

# -- Greet the customer
print('''

Welcome to WacBucks, the PTech Coffee Cafe.
My name is CuppaJoe, your coffee-robot extraordinaire!
''')
customerName = input("And may I have your name, please? : ")

# -- Take the customer's order
print('''
What I can I get for you today?

=== Our Menu ===
   Hot Drinks                  Bakery Items
 1. Black Coffee             4. Bagel w/ Cream Cheese
 2. Espresso                 5. Croissant
 3. Pumpkin Spice Latte      6. Pumpkin Bread
 
Please order one drink and, if you want, one bakery item.
''')
isOrdering = True      # --- Drink Order
drinkOrder = bakeryOrder = ""
menuChoice = input("First, what would you like to drink? : ")
while isOrdering:
    if menuChoice == "1":
        print("Black Coffee, great choice!")
        drinkOrder = "Black Coffee"
        isOrdering = False
    elif menuChoice == "2":
        print("Espresso, got it!")
        drinkOrder = "Espresso"
        isOrdering = False
    elif menuChoice == "3":
        print("Pumpkin Spice Latte, I love Autumn!")
        drinkOrder = "Pumpkin Spice Latte"
        isOrdering = False
    else :
        print("Please choose 1, 2, or 3")
        menuChoice = input("What would you like to drink? : ")

# --- Whipped Cream on the drink
menuChoice = input("and, would you like cream on that? (y/N): ")
if menuChoice == "y":
    print("Sure, you deserve it!")
    drinkOrder = drinkOrder + " with Whipped Cream on top"

isOrdering = True      # -- Bakery order
menuChoice = input("And would you like an item from the bakery? : ")
while isOrdering:
    if menuChoice == "4":
        print("I'll toast one for you right now!")
        bakeryOrder = "and a Bagel"
        isOrdering = False
    elif menuChoice == "5":
        print("Those were baked fresh just this morning!")
        bakeryOrder = "and a Croissant"
        isOrdering = False
    elif menuChoice == "6":
        print("Excellent choice - I love the fresh spices!")
        bakeryOrder = "and a fresh slice of Pumpkin Bread"
        isOrdering = False
    elif menuChoice == "n":
        isOrdering = False
    else :
        print("Please choose 4, 5, 6, or 'n' for No.")
        menuChoice = input("Would you like an item from the bakery? : ")

# --- Pause for prep time
print(" === That'll be ready in just a few minutes...\n")

# --- Order up!
print(f"I've got an order up for {customerName}!")
print(f"That's one {drinkOrder} {bakeryOrder}.\n")
print("That's for visiting WacBucks - please enjoy!\n\n")

