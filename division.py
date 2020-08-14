def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Division by zero not possible")

        # a = int(input("Enter one Number: "))
        # b = int((input("Enter second Number: ")))

        # div_result = divide(a, b)
        # print(f'Result of division of {a} and {b} = {div_result}')
