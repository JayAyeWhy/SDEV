# Ja'xon Sibley 10/30/2023 makes an order array #
print("Enter the first integer: ")
first_integer = input()
print("Enter the second integer: ")
second_integer = input()
print("Enter the third integer: ")
third_integer = input()
lowest = 0
biggest = 0
clone = 0
if first_integer > second_integer:
    biggest = first_integer
    lowest = second_integer
else:
    biggest = second_integer
    lowest = first_integer
if third_integer > biggest:
    clone = biggest
    biggest = third_integer
elif third_integer < lowest:
    clone = lowest
    lowest = third_integer
    
print("The ordered list of integers is: " + str(lowest) + "," + str(clone) + "," + str(biggest))
