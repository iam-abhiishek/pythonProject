num1 = int(input("enter a num1\n"))
num2 = int(input("enter a num2\n"))
num3 = int(input("enter a num3\n"))

if num1 > num2 and num1 > num3:
    print("num1 is greater", num1)
elif num2 > num3:
    print("num2 is greater", num2)
else:
    print("num3 is greater", num3)