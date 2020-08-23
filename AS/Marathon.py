RaceHours = int(input("Hours:"))
RaceMinutes = int(input("Minutes:"))
RaceSeconds = int(input("Seconds:"))
BestTime = int(input("Best time in seconds:"))

TotalSeconds = RaceHours * 3600 + RaceHours * 60 + RaceSeconds
if TotalSeconds > BestTime:
    print("Personal best time is unchanged")
elif TotalSeconds < BestTime:
    print("New personal  best time")
else:
    print("Equals personal best time")

print("Your result is ", TotalSeconds, "seconds")
