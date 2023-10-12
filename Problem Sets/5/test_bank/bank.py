def main():
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")

def value(user_input):

    user_input = user_input.lower().strip()

    if len(user_input) == 0:
        return 100

    elif user_input[:5] == "hello":
        return 0

    elif user_input[0] == "h":
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()