import random


def main():

    lvl = get_level()

    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        result = x + y

        attempt = 0
        while True and attempt <= 3:
            if attempt >= 3:
                print(f"{x} + {y} = {result}")
                break

            user_ans = int(input(f"{x} + {y} = "))
            if user_ans == result:
                score = score + 1
                break

            else:
                attempt = attempt + 1
                print("EEE")

    print("Score:", score)




def get_level():
    while True:
        try:

            level = input("Level:")
            level = int(level)

        except ValueError:
            continue

        if level < 1:
            continue

        elif level > 3:
            continue

        else:
            return level


def generate_integer(lvl):
    if lvl == 1:
        return random.randint(0, 9)

    elif lvl == 2:
        return random.randint(10, 99)

    elif lvl == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()