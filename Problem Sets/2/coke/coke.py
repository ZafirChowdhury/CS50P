cost = 50
accepted_coin = [5, 10, 25]

while cost > 1:
    user_input = int(input("Insert Coin:  "))

    if user_input in accepted_coin:
        cost = cost - user_input

    if cost > 0:
        print("Amount Due:",cost)


print("Change Owed:",cost*-1)