def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    x = False
    for i in range(len(s)):
        if not s[i].isalpha():
            x = i
            break

    if x:

        if not s[x:].isdigit():
            return False

        if s[x] == "0":
            return False

    return True


if __name__ == "__main__":
    main()