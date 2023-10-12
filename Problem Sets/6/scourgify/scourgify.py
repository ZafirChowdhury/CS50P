import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    if "." not in sys.argv[1] and "." not in sys.argv[2]:
        sys.exit("File extension missing")

    else:
        name, extension = sys.argv[1].split(".")
        name2, extension2 = sys.argv[2].split(".")
        if extension != "csv" or extension2 != "csv":
            sys.exit("Not a CSV file")

        else:
            before = []
            after = [["first", "last", "house"]]
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    for row in reader:
                        before.append(row)

                for row in before[1:]:
                    last, first = row[0].split(",")
                    house = row[1]
                    after.append([first.strip(), last, house])

                with open(sys.argv[2], "w") as file:
                    w = csv.writer(file)
                    for row in after:
                        w.writerow(row)

            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")
