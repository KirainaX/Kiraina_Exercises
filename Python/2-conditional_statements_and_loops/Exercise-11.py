row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
mult_list = [[0 for col in range(col_num)] for row in range(row_num)] # hoka kat3ty list 0 kolhom

for row in range(row_num):
    for col in range(col_num):
        mult_list[row][col] = row * col
print(mult_list)
