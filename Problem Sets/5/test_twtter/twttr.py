def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(user_input):
    vowels = ["a", "e", "i", "o", "u"]

    output_str = ""

    for i in user_input:
        if i.lower() in vowels:
            pass
        else:
            output_str = output_str + i

    return output_str


if __name__ == "__main__":
    main()
