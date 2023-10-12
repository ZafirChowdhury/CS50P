def main():
    user_input = input("What time is it? ")
    time = convert(user_input)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    time = time.split(":")
    hour = float(time[0])
    min = float(time[1])

    con = 1/60

    return hour+(min*con)

    #60 - 1
    #1  - 1/60
    #30 - 30 * 1/60

if __name__ == "__main__":
    main()