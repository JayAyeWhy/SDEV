##This program will make the user to create a task list. they can add delete and see their list with their input using the console
def Add_Task(list) -> list:
    UserInput = input("Add the task you would like." + "\n")
    list.append(UserInput)
    return list
def Delete_Task(list):
    UserInput = input("Type the task you would like to delete.")
    FoundInList = False                     ## This will check if the item if found in list
    for i in range(0,len(list),1):
        if UserInput == list[i]:
            list.remove(UserInput)
            FoundInList = True
    if FoundInList == False:
        print("That wasn't a task in the list")
        
    return list
def Display_Tasks(list) -> list:
    if list == []:
        print("Your list is empty.")
    else:
        for i in range(0,len(list),1):
             print(str(i+1) + "." + str(list[i]))
    return list
def Quit():
    print("You Selected to Quit")
    pass
def Get_UserInput():
    UserInput = input("Select one of the following: " + "\n 1. Add Task" + "\n 2. Delete Task" +  "\n 3. Display Tasks" +  "\n 4. Quit" + "\n" )

    return UserInput

def Options(choice = 0, list = []) -> int:   ## These are option parameters
    try:                             ## Incase the enter a non number this will catch it a say error
         choice = int(Get_UserInput())
    except:
         print("Error")
    if choice == 1:
            Add_Task(list)
            Options(None,list)
    elif choice == 2:
            Delete_Task(list)
            Options(None,list)
    elif choice == 3:
            Display_Tasks(list)
            Options(None,list)
    elif choice == 4:
        Quit()
    else:
        print("You have enter an invalid response.")
        Options()



def main():
    Options()
if __name__ == "__main__":
    main()

    

    

