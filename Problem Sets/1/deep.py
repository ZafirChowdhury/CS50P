user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?" ).strip().lower()
yes_input_list = ["42", "forty-two", "forty two", "fortytwo"]
if user_input in yes_input_list:
    print("Yes")
else:
    print("No")