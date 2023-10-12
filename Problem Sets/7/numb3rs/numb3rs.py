import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()

    if not "." in ip:
        return False

    dot_count = 0
    for i in ip:
        if i == ".":
            dot_count = dot_count + 1

    if dot_count != 3:
        return False

    numbers = ip.split(".")

    for i in numbers:
        if i.isnumeric() and 0 <= int(i) <= 255:
            pass
        else:
            return False

    return True


if __name__ == "__main__":
    main()