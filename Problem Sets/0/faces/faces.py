user_input = input().split()

face_table = {
    ":)":"🙂",
    ":(":"🙁"
}

for i in user_input:
    if i in face_table:
        print(face_table[i], end=" ")
    else:
        print(i, end=" ")