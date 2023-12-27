white = ""
for row in range(0, 7):
    for colum in range(0, 7):
        if (colum == 1 or (row == 6 and colum != 0 and colum < 6)):
            white = white + "*"
        else:
            white = white + " "
    white = white + "\n"
print(white)