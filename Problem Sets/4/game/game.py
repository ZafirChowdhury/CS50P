import random
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

number = random.randint(1, n)

while True:

    while True:
        try:

            ans = int(input("Guess: "))
            if ans > 0:
                break

        except ValueError:
            pass

    if number == ans:
        print("Just right!")
        break

    elif number > ans:
        print("Too small!")

    elif number < ans:
        print("Too large!")