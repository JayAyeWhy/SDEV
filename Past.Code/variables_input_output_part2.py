print("Enter your score out of 15: ")
Score = input()
Percent = ((int(Score)/15)* 100)
print("Your final score was " + str(int(Percent)) + "%")
## Did some fixing to make the percent look like a real percent by rounding it up. ##