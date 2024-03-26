try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the secon number: "))
    div = a/b
    print("The result is ", div)
except ZeroDivisionError:
    print("The number cannot be divided by 0")

print("The program has ended")