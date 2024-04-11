class AllTables():
    def __init__(self, AmountOfTables):
        self.all_tables = []
    def addtable(self, Tables):
        table_number = input("Type the table number")
        Table(table_number)
        self.all_tables.append(Table)
    def display_tables():
        print(AllTables.all_tables[0].table_number)

class Table():
    def __init__(self, table_number): #, seats, in_use, order_taken):
        self.table_number = table_number


AllTables.addtable()
AllTables.display_tables()