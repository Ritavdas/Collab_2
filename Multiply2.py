#Python program to multiply two numbers using function
def multiply_num(a,b):
    multiply=a*b

    return multiply;
num1=int(input("input the number one: "))#input from user for num1
num2=int(input("input the number two: "))#input from user for num2
print("The product is",multiply_num(num1,num2))