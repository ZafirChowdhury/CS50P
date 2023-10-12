def check(s):
    s = s.strip()

    if s.startswith("#"):
        return False

    if s.isspace():
        return False

    if s == "":
        return False

    return True

import sys
if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 2:
    program_name = sys.argv[1]

    if "." in program_name:
        extension = program_name.split(".")
        extension = extension[1]

    else:
        sys.exit("File name lacks extension")

    if extension != "py":
        sys.exit("Not a Python file")

    try:

        line_count = 0
        with open(program_name) as file:
            for i in file:
                if check(i):
                    line_count = line_count + 1

        print(line_count)


    except FileNotFoundError:
        sys.exit("File does not exist")