HomeTeamName = input("Home Team Name:")
HomeRuns = int(input("HomeRuns:"))
AwayTeamName = input("Away Team Name:")
AwayRuns = int(input("AwayRuns:"))

if HomeRuns > AwayRuns:
    RunDifference = HomeRuns - AwayRuns
    WinningTeamName = HomeTeamName
elif AwayRuns > HomeRuns:
    RunDifference = AwayRuns - HomeRuns
    WinningTeamName = AwayTeamName
else:
    print("It's tie now")

print("Winning Team is ", WinningTeamName, " who scored ", RunDifference, " more runs")
