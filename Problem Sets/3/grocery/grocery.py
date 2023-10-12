items = {}

while True:
    try:
        user_input = input().upper()
        if items.get(user_input, None):
            items[user_input] = items[user_input] + 1
        else:
            items[user_input] = 1
    except EOFError:
        break

items = dict(sorted(items.items()))

for i, j in items.items():
    print(f"{j} {i}")