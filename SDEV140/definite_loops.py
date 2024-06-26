## Ja'xon Sibley, 11/6/2023. This programs makes pyramids foward and reverse in the console with numbers

def get_input() -> int:
    UserInput = int(input("Enter the height of the pyramid: "))
    return UserInput

def write_pyramid_row(row: int, height: int) -> None:
    counter = row                                   ## counter is just a copy of row so that i wont change the row varible within my function
    for i in range(0,height-row,1):
        print(" ", end='')
    for i in range(0 ,row, 1):
        if row == 1:                           ## This if statement checks if its the last loop so that it wont do another end=''. It will allow the next print to be on new line
            print(i+1)
        else:
            print(i+1,end='')
    if row >= 2:
        for i in range(1, row,1):
            if row == i+1:
                counter -= 1                   ## This if statement checks if its the last loop so that it wont do another end=''. It will allow the next print to be on new line
                print(counter) 
            else:
                counter -= 1                    
                print(counter,end='')

    


def create_pyramid(height: int) -> None:
    if height <= -1:                            ##This will check if its a reverse pyramid
        Negtrue = True
        height = height * -1
    else:
        Negtrue = False
    for i in range(0,height,1):
        if Negtrue:
            write_pyramid_row(height-i, height)
        else:
            write_pyramid_row(i+1, height)
    

    
if __name__ == "__main__":
    height = get_input()
    create_pyramid(height)
    

