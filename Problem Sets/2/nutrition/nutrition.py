user_input = input("Item: ").lower().strip()

cals = {
    "apple":130,
    "avocado":50,
    "sweet cherries":100,
    "kiwifruit":90,
    "pear":100
}

if cals.get(user_input):
    print("Calories: ",cals.get(user_input))