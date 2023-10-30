from data import resources, MENU


def process_coin():
    print("Please insert coins.")
    quater = 0.25 * int(input("how many quarters?: "))
    dime = 0.10 * int(input("how many dimes?: "))
    nickle = 0.05 * int(input("how many nickles?: "))
    pennie = 0.01 * int(input("how many pennies?: "))
    total = quater + dime + nickle + pennie
    return round(total, 2 )

PROFIT = 0
def make_coffe(coffe):
    coffe_made = False
    recipe = MENU[coffe]["ingredients"]
    for ingredient, amount in recipe.items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry there is not enough {ingredient}.")
            coffe_made = False
            break
        else : 
            resources[ingredient] -= amount
            coffe_made = True
    return coffe_made


def check_transaction(money,coffe):
    cost = MENU[coffe]["cost"]
    change = money - cost
    go_ahead = False
    if change > 0:
        print(f"Here is ${change} in change.")
        go_ahead = True
    else :
        print("Sorry that's not enough money. Money refunded.")
    return go_ahead


while True:
    while True :
        response = input("What would you like? (espresso/latte/cappuccino):").lower()
        if response in ["espresso", "latte", "cappuccino", "off", "report"]:
            break
        else : 
            print("Invalid input. Please enter a valid input.")
    if response in ["espresso", "latte", "cappuccino"]:
        if make_coffe(response) is True:
            money = process_coin()
            if check_transaction(money, response) is True:
                print(f"Here is your {response} ☕️. Enjoy!")
                PROFIT = PROFIT + MENU[response]["cost"]
    elif response == "report" :
        resources["money"] = PROFIT
        for ingredient, amount in resources.items():
            if ingredient in ["water", "milk"]:
                print(f"{ingredient}: {amount}ml")
            elif ingredient == "coffee" :
                print(f"{ingredient}: {amount}g")
            else :
                print(f"{ingredient}: ${amount}")
    else : 
        break
