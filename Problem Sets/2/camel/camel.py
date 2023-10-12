user_input = input("cameCase: " )
output_str = ""

for i in user_input:
    if i == " ":
        output_str = output_str + "_"

    elif i.isupper() and not i == user_input[0]:
        output_str = output_str + "_" + i.lower()

    else:
        output_str = output_str + i

print(output_str)