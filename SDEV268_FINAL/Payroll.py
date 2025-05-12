import datetime

#Set varibles
MEDICAL_SINGLE = 50
MEDICAL_FAMILY = 100
MEDICARE = 0.0145
DEPENDENT_STIPEND = 45
STATE_TAX = 0.0315
FEDERAL_TAX = 0.0765
SOCIAL_SECURITY = 0.062

timesheets = {}

def CheckAge(dob):
    birthday = datetime.datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.datetime.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

def login():
    id = input("Enter User ID: ")
    password = input("Enter Password: ")
    type = input("Login as (Admin/Employee): ")

    if type == "Admin" and admin_credentials.get(id) == password:
        return "Admin", id
    elif type == "Employee":
        if id in employees:
            dob = input("Enter DOB (YYYY-MM-DD): ")
            if employees[id]["dob"] == dob:
                return "Employee", id
    print("Invalid credentials")
    return None, None

#ADMIN LOGIN
admin_credentials = {"Admin": "admin"}

def AdminMenu():
    while True:
        print("1. View Employees\n2. Calculate Payroll\n3. Add/Edit Employee\n4. Logout")
        choice = input("Choose: ")
        if choice == "1":
            for eid, emp in employees.items():
                print(f"{eid}: {emp['first_name']} {emp['last_name']}")
        elif choice == "2":
            payroll()
        elif choice == "3":
            EditEmployees()
        elif choice == "4":
            break
        else:
            print("Invalid option")

def EmployeeMenu(id):
    while True:
        print("1. Enter Time Worked\n2. View Paycheck Estimate\n3. Logout")
        choice = input("Choose: ")
        if choice == "1":
            hours(id)
        elif choice == "2":
            CalculatePay(id)
        elif choice == "3":
            break
        else:
            print("Invalid option")

def hours(emp_id):
    print("Enter hours for 7 days (Mon to Sun)")
    hours = []
    for i in range(7):
        h = float(input(f"Day {i+1} hours: "))
        hours.append(h)
    timesheets[emp_id] = hours
    print("Hours saved")

def CalculatePay(id):
    emp = employees[id]
    hours = timesheets.get(id, [8]*5 + [0, 0] if emp['pay'] == "Salary" else [0]*7)
    gross = 0.0

    if emp["pay"] == "Hourly":
        for i, h in enumerate(hours):
            if i == 5 or i == 6:  
                gross += h * emp['salary'] * 1.5
            else:
                gross += emp['salary'] * (8 if h <= 8 else 8 + (h - 8) * 1.5)
    else:
        gross = emp['salary']  

    deductions = 0.0
    med_cost = MEDICAL_SINGLE if emp['medical'] == "Single" else MEDICAL_FAMILY
    dependent_bonus = emp['dependents'] * DEPENDENT_STIPEND
    taxable_income = gross - med_cost - dependent_bonus

    deductions += taxable_income * STATE_TAX
    deductions += taxable_income * FEDERAL_TAX
    deductions += taxable_income * SOCIAL_SECURITY
    deductions += taxable_income * MEDICARE
    deductions += med_cost

    net = gross - deductions
    print(f"\nGross: ${gross:.2f}")
    print(f"Deductions: ${deductions:.2f}")
    print(f"Net Pay: ${net:.2f}")

def payroll():
    print("\nREPORT")
    for eid in employees:
        if employees[eid]["status"] == "Active":
            print(f"\nEmployee: {eid} - {employees[eid]['first_name']}")
            CalculatePay(eid)

def EditEmployees():
    eid = input("Enter Employee ID: ")
    if eid not in employees:
        employees[eid] = {}
    employees[eid]["first_name"] = input("First Name: ")
    employees[eid]["last_name"] = input("Last Name: ")
    employees[eid]["dob"] = input("DOB (YYYY-MM-DD): ")
    age = CheckAge(employees[eid]["dob"])
    if age < 18:
        print("Employee must be at least 18.")
        return
    employees[eid]["email"] = input("Email: ")
    employees[eid]["gender"] = input("Gender (M/F): ")
    employees[eid]["pay_type"] = input("Pay Type (Salary/Hourly): ")
    employees[eid]["salary"] = float(input("Salary/hourly rate: "))
    employees[eid]["dependents"] = int(input("Dependents: "))
    employees[eid]["medical"] = input("Medical Plan (Single/Family): ")
    employees[eid]["status"] = input("Status (Active/Terminated): ")
    print("Employee saved")

employees = {
    "E001": {
        "first_name": "John", "last_name": "Snow", "dob": "2000-05-15",
        "email": "johnsnow@gmail", "gender": "M", "pay_type": "Hourly",
        "salary": 100.0, "dependents": 1, "medical": "Family", "status": "Active"
    },
    "E002": {
        "first_name": "Sarah", "last_name": "Brown", "dob": "1999-01-12",
        "email": "sarahbrown@gmail", "gender": "F", "pay_type": "Salary",
        "salary": 1000.0, "dependents": 0, "medical": "Single", "status": "Active"
    },
}

while True:
        print("PAYROLL SYSTEM")
        print("1.Login\n2.Exit")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            role, uid = login()
            if role == "Admin":
                AdminMenu()
            elif role == "Employee":
                EmployeeMenu(uid)
        elif choice == "2":
            break
        else:
            print("Invalid")


