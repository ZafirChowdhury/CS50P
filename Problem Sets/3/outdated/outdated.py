def retard_code(date):
    pp = ""

    for i in date:
        if i != "/":
            pp = i + pp

    return pp.isnumeric()

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()

    if "," in date and not date[0].isnumeric():
        date = date.split(",")

        temp = date[0].split(" ")
        month = temp[0]

        day = temp[1]
        if int(day) < 10:
            day = "0"+day

        year = date[1].strip()

        imonth = str(int(month_list.index(month))+1)
        if int(imonth) < 10:
            imonth = "0"+imonth

        if month in month_list and int(day) <= 31:
            print(f"{year}-{imonth}-{day}")
            break

    elif "/" in date and retard_code(date):
        date = date.split("/")

        month = date[0]
        if int(month) < 10:
            month = "0"+month

        day = date[1]
        if int(day) < 10:
            day = "0"+day

        year = date[2]

        if int(month) <= 12 and int(day) <= 31:
            print(f"{year}-{month}-{day}")
            break

