vowels = ["a", "e", "i", "o", "u"]
user_input = input("Input: ")

output_str = ""

for i in user_input:
    if i.lower() in vowels:
        pass
    else:
        output_str = output_str + i

print("Output: ",output_str)