loop = True
while loop:
    last_name = input("Please input your last name: ")
    if last_name == "ZZZ":
        loop = False
        print("You have quit")
    else:
        first_name = input("Please input your first name: ")
        gpa = float( input('Please input your GPA as a float number: '))
        if gpa > 3.5:
            print(first_name + ", You have made the Dean List!")
        if gpa > 3.25:
            print(first_name + ", You have meade the Honor Roll")
        else:
            print(first_name + ", You didnt make any list")
    

