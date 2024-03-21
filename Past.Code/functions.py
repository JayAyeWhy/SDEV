## Jay Sibley 11/1/2023, Calculate distance function ##

import math
def CalcDistance(x1,y1,x2,y2):
        distance = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
        distance = round(distance, 2)
        return distance

def main():
    print("Enter x1 coordinate: ")
    x1 = int(input())
    print("Enter y1 coordinate: ")
    y1 = int(input())
    print("Enter x2 coordinate: ")
    x2 = int(input())
    print("Enter y2 coordinate: ")
    y2 = int(input())
    print("The distance bettween these points is " + str((CalcDistance(x1,y1,x2,y2))))
main()
