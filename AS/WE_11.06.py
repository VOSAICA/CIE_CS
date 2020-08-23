NextNumber = int(input("Enter a number: "))

Temp = NextNumber
while NextNumber != 0:
    NextNumber = int(input("Enter a number: "))
    if NextNumber > Temp:
        Temp = NextNumber
print("The biggest number is ", Temp)
