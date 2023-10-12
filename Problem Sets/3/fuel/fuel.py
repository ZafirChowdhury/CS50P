while True:
    try:

        fraction = input("Fraction: ").split("/")

        x = int(fraction[0])
        y = int(fraction[1])

        if x <= y:
            break

    except (ValueError, IndexError) as _:
        pass

percentage = round(x/y * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")