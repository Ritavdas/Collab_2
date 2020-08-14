# This is the addition function
from division import divide
from Multiply2 import multiply
from Subtract import subtract


def add(num1, num2):
    return num1 + num2


def power(num1, num2):
    return num1 ** num2


print("\nWELCOME \tTO \tMY \tCALCULATOR\n")

a = True

while a != '':
    answer = input(
        "Which function do you want to use? \n 1. Add \n 2. Subtract \n 3. Multiplty \n 4. Divide \n 5. Power \n =>  ")

    if answer == '':  # IF THERE'S NO INPUT THE CALCULATOR STOPS
        a = ''
        print("Thank you for using my Calculator :) \n")
        break

    a = float(input("Enter one Number: "))
    b = float(input("Enter second Number: "))

    if answer == '1':                   # ADDITION FUNCTION
        result_add = add(a, b)
        print(f'\nResult of addition of {a} and {b} =  {result_add} \n')

    elif answer == '2':                 # SUBTRACTION FUNCTION
        result_subtract = subtract(a, b)
        print(
            f'\nResult of subtraction of {a} and {b} =  {result_subtract} \n')

    elif answer == '3':                 # MULTIPLICATION FUNCTION
        result_multiply = multiply(a, b)
        print(
            f'\nResult of multiplication of {a} and {b} =  {result_multiply} \n')

    elif answer == '4':                 # DIVISION FUNCTION
        result_divide = divide(a, b)
        print(f'\nResult of division of {a} and {b} =  {result_divide} \n')

    elif answer == '5':                 # POWER FUNCTION
        result_power = power(a, b)
        print(f'\nResult of {a} to  the power of {b} =  {result_power} \n')

    else:  # IF INPUT ISN'T 1,2,3,4,5 IT'LL BE TERMED AS INVALID
        print("\nInvalid Input try again \n")


# add_result = add(a, b)
# print(f'Result of addition of {a} and {b} =  {add_result}')
