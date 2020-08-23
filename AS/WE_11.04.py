Temp = int(input("Please enter your first number: "))

Counter = 1
while Counter < 10:
    NextNumber = int(input("Please enter your next number: "))
    if NextNumber > Temp:
        Temp = NextNumber
    Counter = Counter + 1
print("The largest number is ", Temp)
