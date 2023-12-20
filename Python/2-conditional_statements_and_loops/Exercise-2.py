def Fahrenheit_Celsius():
    type = input("Enter the unit you want to convert to 'c' for Celsius and 'f' for Fahrenheit : ")
    for i in type:
        if (type == 'c') or (type == 'f'):
            if type == 'c':
                degree = int(input("Enter temperatures of Fahrenheit: "))
            else:
                degree = int(input("Enter temperatures of Celsius: "))
        else:
            print("the unit u enter is not one of the unit")
            Fahrenheit_Celsius()

    c = 0
    f = 0
    for i in type:
        if i == 'c':
            c = (degree - 32) * (5 / 9) 
            print("{}°F is {} in Celsius".format(degree, c))
            break
        elif i == 'f':
            f = (degree * (9 / 5)) + 32
            print("{}°C is {} in Fahrenheit".format(degree, f))
            break


Fahrenheit_Celsius()
