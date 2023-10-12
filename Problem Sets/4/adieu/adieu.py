name_list = []

while True:
    try:

        name = input("Name: ").strip()
        name_list.append(name)

    except EOFError:
        break

output = "Adieu, adieu, to"
for i in name_list:
    if i != name_list[-1]:
        output = output + " " + i + ","

    elif i == name_list[-1] and len(name_list) > 1:
        output = output +  " " + "and" + " " + i

    elif len(name_list) == 1:
        output = output +  " " + name_list[0]

print(output)