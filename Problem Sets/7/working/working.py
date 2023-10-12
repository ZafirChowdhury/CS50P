def main():
    try:
        print(convert(input("Hours: ").strip()))
    except IndexError:
        raise ValueError

def convert(s):
    str_list = s.split(" ")

    if not "to" in str_list:
        raise ValueError

    if ":" in s:
        start_hour, start_min = str_list[0].split(":")
        end_hour, end_min = str_list[3].split(":")

        if (
            not (0 <= int(start_min) <= 59)
            or not (0 <= int(end_min) <= 59)
            or int(start_hour) > 12
            or int(end_hour) > 12
        ):
            raise ValueError

    else:
        start_hour = str_list[0]
        end_hour = str_list[3]

        start_min = "00"
        end_min = "00"

    start_de = str_list[1]
    end_de = str_list[4]

    #9:00 AM to 5:00 PM
    #09:00 to 17:00

    if start_de == "PM":
        start_hour = str(int(start_hour) + 12)

    if end_de == "PM" and end_hour:
        end_hour = str(int(end_hour) + 12)

    if int(start_hour) <= 9:
        start_hour = f"0{start_hour}"

    if int(end_hour) <= 9:
        end_hour = f"0{end_hour}"

    if start_hour == "12" and start_de == "AM":
        start_hour = "00"

    if int(end_hour) == 24:
        end_hour = "12"

    return f"{start_hour}:{start_min} to {end_hour}:{end_min}"


if __name__ == "__main__":
    main()