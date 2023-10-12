from datetime import date
import sys
import inflect
p = inflect.engine()


def date_sub(date_of_birth):
    days = str(date.today() - date_of_birth)
    days = days.split(" ")
    days = days[0]

    mins = int(days) * 24 * 60

    return str(mins)

def main():
    try:
        date_of_birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    sub = date_sub(date_of_birth)
    in_words = p.number_to_words(sub, andword="")

    print(f"{in_words.capitalize()} minutes")

if __name__ == "__main__":
    main()