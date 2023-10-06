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
            "oatmilk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "oatmilk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "oatmilk": 200,
    "coffee": 100,
}

stored_currency = {
  "quarters": 0,
  "dimes": 0,
  "nickels": 0,
  "pennies": 0
}

consumer_choice = "";


def get_consumer_choice(error_message = ""):
  global consumer_choice
  prompt = " Which kind of coffee would you like? (espresso | latte | cappuccino)\n"

  if error_message != "":
    consumer_choice = input(error_message + prompt)
  else:
    consumer_choice = input("Welcome!" + prompt)
  
  return consumer_choice

def print_report():
  print("Ingredients remaining")
  print("water: " + str(resources["water"]) + "ml")
  print("coffee: " + str(resources["coffee"]) + "ml")
  print("oatmilk: " + str(resources["oatmilk"]) + "ml")
  print("Total currency")
  print("quarters: " +str(stored_currency["quarters"]))
  print("dimes: " +str(stored_currency["dimes"]))
  print("nickels: " +str(stored_currency["nickels"]))
  print("pennies: " +str(stored_currency["pennies"]))

  input("Press any button to continue")


def validate_choice(choice):
  valid_choice = False
  valid_options = ["report", "espresso", "latte", "cappuccino"]

  if choice == "report":
    print_report()
    get_consumer_choice();

  for option in valid_options:
    if option == choice:
      valid_choice = True

  if valid_choice != True:
    new_choice = get_consumer_choice(choice + " is invalid.")
    validate_choice(new_choice)


def validate_sufficient_resources(choice):
  resource_cost = MENU[choice]["ingredients"]

  if choice == "espresso" and resource_cost["water"] > resources["water"] or resource_cost["coffee"] > resources["coffee"]:
    new_choice = get_consumer_choice("Insufficient resources to make " + choice)
    validate_choice(new_choice)
    validate_sufficient_resources(new_choice)
  elif resource_cost["oatmilk"] > resources["oatmilk"] or resource_cost["water"] > resources["water"] or resource_cost["coffee"] > resources["coffee"]:
    new_choice = get_consumer_choice("Insufficient resources to make " + choice)
    validate_choice(new_choice)
    validate_sufficient_resources(new_choice)


def get_payment(choice):
  choice_cost = MENU[choice]["cost"]

  print(choice + " costs $" + str(choice_cost) + "0. Input your payment.")

  return {
    "quarters": int(input("Quarters:")),
    "dimes": int(input("Dimes:")),
    "nickels": int(input("Nickels:")),
    "pennies": int(input("Pennies:"))
  }

def update_machine(choice, payment):
  stored_currency["quarters"] += payment["quarters"]
  stored_currency["dimes"] += payment["dimes"]
  stored_currency["nickels"] += payment["nickels"]
  stored_currency["pennies"] += payment["pennies"]

  resources["water"] -= MENU[choice]["ingredients"]["water"]
  resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
  if choice != "espresso":
    resources["oatmilk"] -= MENU[choice]["ingredients"]["oatmilk"]


def validate_payment(payment):
  cost = MENU[consumer_choice]["cost"]

  total_payment = payment["quarters"] * .25 + payment["dimes"] * .10 + payment["nickels"] * .05 + payment["pennies"] * .01

  if cost > total_payment:
    get_consumer_choice('Insufficient funds.')

  print("Thank you, here is your change. " + str(total_payment - cost))
  update_machine(consumer_choice, payment)
  get_consumer_choice();


consumer_choice = get_consumer_choice()

validate_choice(consumer_choice)

validate_sufficient_resources(consumer_choice)

payment = get_payment(consumer_choice)

validate_payment(payment)