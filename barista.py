#
#       project: barista.py
#        author: Charles J McDonald <cmcdonald@woonsocketschools.com>
#  last updated: 09/27/2024
#
#   description: Meet Cuppa Joe, the robot barista
#       version: 1.1

# -- Greet the customer
print('''
Welcome to WacBucks, the PTech Coffee Cafe.
My name is CuppaJoe, your coffee-robot extraordinaire! \n
''')
customerName = input("And may I have your name, please? : ")

# -- Take the customer's order
print('''
What I can I get for you today?

=== Our Menu ===
      Hot Drinks                           Bakery Items
 1. Black Coffee          $0.75      4. Bagel w/ Cream Cheese   $2.50
 2. Espresso              $1.99      5. Croissant               $1.99
 3. Pumpkin Spice Latte   $2.99      6. Pumpkin Bread           $1.50

Please order one drink and, if you want, one bakery item.
''')
isOrdering = True  # --- Drink Order
drinkOrder = bakeryOrder = ""
costOfOrder = float(0.00)
menuChoice = input("First, what would you like to drink? : ")
while isOrdering:
    if menuChoice == "1":
        print("Black Coffee, great choice!")
        drinkOrder = "Black Coffee"
        costOfOrder += 0.75
        isOrdering = False
    elif menuChoice == "2":
        print("Espresso, got it!")
        drinkOrder = "Espresso"
        costOfOrder += 1.99
        isOrdering = False
    elif menuChoice == "3":
        print("Pumpkin Spice Latte, I love Autumn!")
        drinkOrder = "Pumpkin Spice Latte"
        costOfOrder += 2.99
        isOrdering = False
    else:
        print("Please choose 1, 2, or 3")
        menuChoice = input("What would you like to drink? : ")

# --- Whipped Cream on the drink
menuChoice = input("and, would you like cream on that? (y/N): ")
if menuChoice == "y":
    print("Sure, you deserve it!")
    drinkOrder = drinkOrder + " with Whipped Cream on top"
    costOfOrder += 0.99

isOrdering = True  # -- Bakery order
menuChoice = input("And would you like an item from the bakery? : ")
while isOrdering:
    if menuChoice == "4":
        print("I'll toast one for you right now!")
        bakeryOrder = "and a Bagel"
        costOfOrder += 2.50
        isOrdering = False
    elif menuChoice == "5":
        print("Those were baked fresh just this morning!")
        bakeryOrder = "and a Croissant"
        costOfOrder += 1.99
        isOrdering = False
    elif menuChoice == "6":
        print("Excellent choice - I love the fresh spices!")
        bakeryOrder = "and a fresh slice of Pumpkin Bread"
        costOfOrder += 1.50
        isOrdering = False
    elif menuChoice == "n":
        isOrdering = False
    else:
        print("Please choose 4, 5, 6, or 'n' for No.")
        menuChoice = input("Would you like an item from the bakery? : ")

# --- Pause for prep time
print("\n === That'll be ready in just a few minutes...\n")

# --- Calculate total cost with 7% sales tax.
costOfOrder = round(costOfOrder * 1.07, 2)

# --- Order up!
print(f"I've got an order up for {customerName}!")
print(f"That's one {drinkOrder} {bakeryOrder}. Your total comes to ${costOfOrder}.\n")
print("That's for visiting WacBucks - please enjoy!\n\n")

