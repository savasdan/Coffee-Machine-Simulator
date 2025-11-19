from prettytable import PrettyTable

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
x = PrettyTable()
x.add_column("Coffee", ["Espresso", "Latte", "Cappuccino"])
x.add_column("Cost", [1.50, 2.50, 3.00])

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough of {item}!")
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) *0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round( money_received - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy ! ")


is_on = True

while is_on:
    print(x)
    user_pref = input("What would you like? (espresso/latte/cappuccino): ")
    if user_pref == "off":
        is_on = False
    elif user_pref == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_pref]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_pref, drink["ingredients"])
                print("\n"*20)
                print("Hope you came here again to take another one!")
