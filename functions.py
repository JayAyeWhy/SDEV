## Jay Sibley 11/1/2023, Calculate distance function ##
import math
print("Enter x1 coordinate: ")
x1 = int(input())
print("Enter y coordinate: ")
y1 = int(input())
print("Enter x2 coordinate: ")
x2 = int(input())
print("Enter y2 coordinate: ")
y2 = int(input())
distance = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
distance = round(distance, 2)

print("The distance bettween these points is " + str(distance))