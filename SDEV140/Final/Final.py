import csv

def printdata(line):
    for i in line:
        print(line(lines))
    pass
def checkifvalid(line):
    try:
        test = line[1]
        return True
    except:
        return False
    
def FindAccount(id):
    found = False
    with open('Final/patient.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            try:
                if line[0] == id:
                    if checkifvalid(line):

                        for i in range (0, len(line), 1):
                            if i == len(line) - 1:
                                print(line[i] + ";")
                            else:
                                print(line[i] + ";" ,end="")
                            found = True
                    else:
                        print("Skipping account record.")
                        found = True
            except:
                next(csv_reader)
        if found == False:
            print("Invalid Account ID: " + id)
def user():
    bool = True
    while bool:
        Id = input("Enter an ID or 'q' to quit: ")
        if Id != "q":
            FindAccount(Id)
        else:
            bool = False
            print("You have quited")
        




if __name__ == "__main__":
    user()