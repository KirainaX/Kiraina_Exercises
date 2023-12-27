white = ""
for row in range(0, 7):
    for colm in range(0, 7):
        if ((colm == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and colm > 1 and colm < 5) or (row == 3 and colm > 2 and colm < 6) or (colm == 5 and row != 0 and row != 2 and row != 6)):
            white = white + "*"
        else:
            white = white + " "
    white = white + "\n"
print(white)