Temp = int(input("Please enter your first number: "))

Counter = 1
for Counter in range(1, 9, +1):
    NextNumber = int(input("Please enter your next number: "))
    if NextNumber > Temp:
        Temp = NextNumber
print("The largest number is: ", Temp)
