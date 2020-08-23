Number1 = int(input("Enter the first number: "))
Number2 = int(input("Enter the second number: "))
Number3 = int(input("Enter the third number: "))

if Number1 > Number2:
    Temp = Number1
else:
    Temp = Number2
if Number3 > Temp:
    Temp = Number3
print("The largest number is ", Temp)
