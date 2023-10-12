user_input = input("Expression: ").split(" ")

x = float(user_input[0])
y = user_input[1]
z = float(user_input[2])

if y == "+":
    print("{:.1f}".format(x+z))
elif y == "-":
    print("{:.1f}".format(x-z))
elif y == "/":
    print("{:.1f}".format(x/z))
elif y == "*":
    print("{:.1f}".format(x*z))