# This class would hold the array for the all the tables in the resturant
class AllTables():
    # This object will be the list for all the tables objects in resturants. 
    def __init__(self):
        self.all_tables = []
    # Add a table to the list
    def addtable(self, table):
        self.all_tables.append(table)

    # Method will print all the tables in the list with the table # + if its in use + if theres a resevation
    def display_tables(self):
        print(self.all_tables[0].in_use)
        for i in range(len(self.all_tables)):   
            print("Table #" + str(self.all_tables[i].table_number) + ": In_used -" + str(Table.check_in_use(self.all_tables[i])) + ". Resevation -" + str(Table.check_resevation(self.all_tables[i])))
    def next_table_number(self):
        counter = len(self.all_tables)
        return counter + 1
    def addsingle(self):
        table = Table(4,)

class Table():
    def __init__(self, table_number, in_use = False, resevation = None): #, seats, order_taken): ... I havent worked on the other paremeter bc they are not important rn
        self.table_number = table_number
        self.in_use = in_use
        self.resevation = resevation
        # GETTERS
    def get_table_number(self): return self.table_number
    def check_in_use(self): return self.in_use
    def check_resevation(self): 
        if self.resevation == None:
            return False
        else:
            return self.resevation.name
        # SETTERS
    def set_table_number(self,number): self.table_number = number
    def set_in_use(self,bool): self.in_use = bool
    def set_resevation(self,resevation): self.resevation = resevation
        
# This class would hold the resevation object
class Resevation():
    def __init__(self, name):#, time, num_of_people, checked_in):
        self.name = name
    # add a resevation to a table
    def add_resevation(self,table):
        table.resevation = self


# Heres my mess around code here that I used to make sure everything was going aright. feel free to try stuff here
t1 = Table(4)
t2 = Table(2,True)
table_list = AllTables()
table_list.addtable(t2)
table_list.addtable(t1)
table_list.display_tables()
print(Table.check_resevation(t2))
Billy = Resevation("Billy")
t2.set_resevation(Billy)
print(Table.check_resevation(t2))
qwe = table_list.next_table_number()
print(qwe)


# Totally not finished but heres some things for the future code and questions
# - Sort tables by table numbers
# - Make a table method that will create to types of tables :Booth and Party. hopefully with this function we can start getting a ui in the terminal. and maybe automaticly give
# the tables their table number?
# - Make an Order class. This class will have the menu and take the order. It will also add up the total for the table.
# - 
# 
