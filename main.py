MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_is_sufficient(ingredients): #drink['ingredient']
    """Returns TRUE if resources are sufficient, else FALSE"""
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry, not enough {item}")
            return False
    return True

def money_is_sufficient(cost_of_drink,drink_name): # drink['cost'] , choice
    # total_inserted_amount> cost
    quarters = int(input("How many quarters?"))
    dime = int(input("How many dimes?"))
    nickel = int(input("How many nickels?"))
    penny = int(input("How many pennies?"))
    total_inserted_money = (quarters * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    if total_inserted_money>cost_of_drink:
        global profit
        profit+=cost_of_drink
        change=total_inserted_money-cost_of_drink
        print(f"Here is ${change} in change.  ")
        print(f"Enjoy your {drink_name} ☕.  ")
        return True
    else:
        print("Sorry, not enough money. Money Refunded")
        return False

def deduct_resources(ingredients): #drink['ingredient']
    for item in ingredients:
        resources[item] -= ingredients[item]




is_on = True
while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino) : " ).lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Milk : {resources['milk']}")
        print(f"Money : {profit}")

    else:
        drink = MENU[choice]
        if resource_is_sufficient(drink['ingredients']):
            if money_is_sufficient(drink['cost'],choice):
                deduct_resources(drink['ingredients'])








