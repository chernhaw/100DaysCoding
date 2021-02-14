# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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

resources = {
    "water": 308,
    "milk": 20,
    "coffee": 100,
}

money = 0

def checkResource(drink):
    print(f'Drink selected {drink}')


    if (drink == 'expresso'):

        # Check resource needed
        waterNeededDrink = MENU['espresso']['ingredients']['water']
        print (f'Water needed {waterNeededDrink}')
        coffeeNeededForDrink = MENU['espresso']['ingredients']['coffee']
        print(f'Coffee needed {coffeeNeededForDrink}')

        # Check resource left
        waterLeftDrink = resources['water']
        coffeeLeftDrink = resources['coffee']
        print(f'Water left {waterLeftDrink}')
        print(f'Coffee left {coffeeLeftDrink}')

        if (waterLeftDrink<waterNeededDrink):
            return "Sorry there are not enough water"
        elif (coffeeLeftDrink<coffeeNeededForDrink):
            return "Sorry there are not enough coffee"

    elif (drink == 'latte'):

        # Check resource needed
        waterNeededDrink = MENU['latte']['ingredients']['water']
        print (f'Water needed {waterNeededDrink}')
        coffeeNeededForDrink = MENU['latte']['ingredients']['coffee']
        print(f'Coffee needed {coffeeNeededForDrink}')
        milkNeededForDrink = MENU['latte']['ingredients']['coffee']
        print(f'Milk needed {milkNeededForDrink}')

        # Check resource left
        waterLeftDrink = resources['water']
        coffeeLeftDrink = resources['coffee']
        milkLeftDrink = resources['milk']
        print(f'Water left {waterLeftDrink}')
        print(f'Coffee left {coffeeLeftDrink}')
        print(f'Milk left {milkLeftDrink}')

        if (waterLeftDrink<waterNeededDrink):
            return "Sorry there are not enough water"
        elif (coffeeLeftDrink<coffeeNeededForDrink):
            return "Sorry there are not enough coffee"
        elif (milkLeftDrink<milkNeededForDrink):
            return "Sorry there are not enough milk"

    elif (drink == 'cappuccino'):

        # Check resource needed
        waterNeededDrink = MENU['cappuccino']['ingredients']['water']
        print (f'Water needed {waterNeededDrink}')
        coffeeNeededForDrink = MENU['cappuccino']['ingredients']['coffee']
        print(f'Coffee needed {coffeeNeededForDrink}')
        milkNeededForDrink = MENU['cappuccino']['ingredients']['coffee']
        print(f'Milk needed {milkNeededForDrink}')

        # Check resource left
        waterLeftDrink = resources['water']
        coffeeLeftDrink = resources['coffee']
        milkLeftDrink = resources['milk']
        print(f'Water left {waterLeftDrink}')
        print(f'Coffee left {coffeeLeftDrink}')
        print(f'Milk left {milkLeftDrink}')

        if (waterLeftDrink<waterNeededDrink):
            return "Sorry there are not enough water"
        elif (coffeeLeftDrink<coffeeNeededForDrink):
            return "Sorry there are not enough coffee"
        elif (milkLeftDrink<milkNeededForDrink):
            return "Sorry there are not enough milk"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = "On"
    while (order !="Off" or order !="off"):
        order = input("What would you like? (expresso/latte/cappuccino): ")

        if (order == 'report'):
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${money}')

        if (order == 'expresso' or order == 'latte' or order=='cappuccino'):
            print(checkResource(order))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
