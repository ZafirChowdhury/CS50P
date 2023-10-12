import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    if "." not in sys.argv[1]:
        sys.exit("File extension missing")

    else:
        name, extension = sys.argv[1].split(".")
        if extension != "csv":
            sys.exit("Not a CSV file")

        else:
            table = []
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    for row in reader:
                        table.append(row)

            except FileNotFoundError:
                sys.exit("File does not exist")

headers = table[0]
print(tabulate(table[1:], headers, tablefmt="grid"))