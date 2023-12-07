'''
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
'''

def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number # =========================
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers # ====================================
    if original_num == reverse_num:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")


nbr = int(input("Enter a number: "))
palindrome(nbr)
