# This is the addition function

a = int(input("Enter one Number: "))
b = int((input("Enter second Number: ")))


def add(num1, num2):
    return num1 + num2

# print(add(a, b))


add_result = add(a, b)
print(f'Result of addition of {a} and {b} =  {add_result}')
