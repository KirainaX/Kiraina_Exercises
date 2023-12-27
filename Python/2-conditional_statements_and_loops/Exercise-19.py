white = ""
for row in range(0, 7):
    for colm in range(0, 7):
        if (colm == 1 or ((row == 0 or row == 6) and (colm > 1 and colm < 6)) or (row == 3 and colm > 1 and colm < 5)):
            white = white + "*"
        else:
            white = white + " "
    white = white + "\n"

print(white)