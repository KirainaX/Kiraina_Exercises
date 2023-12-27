white_space = ""
for row in range(0, 7):
    for colm in range(0, 7):
        if (colm == 1 or ((row == 0 or row == 6) and (colm > 1 and colm < 5)) or (colm == 5 and row != 0 and row != 6)):
            white_space = white_space + "*"
        else:
            white_space = white_space + " "
    white_space = white_space + "\n"

print(white_space)
