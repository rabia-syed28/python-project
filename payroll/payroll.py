#Imports
import datetime

#Globals
weeks_in_2023 = 52
#PAYE
#Tax credits
employee_tax_credit_2023 = 1775
#Low rate cut off
low_rate_cut_off_2023 = 40000
#Low rate tax - 20%
low_rate_tax_2023 = 0.2
#High rate tax - 40%
high_rate_tax_2023 = 0.4      

#USC
#Standard rates and thresholds of USC for 2023
    #Threshold for 2023     Rate
    #First €12,012          0.5%
    #Next €10,908           2%
    #Next €47,124           4.5%
    #Balance                8%
#PRSI
#Max PRSI credit €12.00 per week
prsi_credit_2023 = 12

#Using different color for font
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = '\033[94m'
RESET = "\033[0m"

#List of Employees
        #First Name
        #Last Name
        #PPSN
        #Personal Tax Credit
        #PRSI Class
        #Annual Salary Amount
        
#Here I declare the information of the First employee
emp1 = {"First Name": "John", "Last Name": "Doe", "PPSN": "1234567AB",
        "Personal Tax Credit": 1775, "PRSI Class": "A",
        "Annual Salary Amount": 25000}

#Here I declare the information of the Second employee
emp2 = {"First Name": "Mary", "Last Name": "Lambe", "PPSN": "7654321ZY",
        "Personal Tax Credit": 1775, "PRSI Class": "A",
        "Annual Salary Amount": 65000}

#Here I declare the information of the Third employee
emp3 = {"First Name": "Peter", "Last Name": "Mark", "PPSN": "9812345CD",
        "Personal Tax Credit": 1775, "PRSI Class": "A",
        "Annual Salary Amount": 45000}

#Here I declare the information of the Fourth employee
emp4 = {"First Name": "John", "Last Name": "Dave", "PPSN": "3324511EF",
        "Personal Tax Credit": 1775, "PRSI Class": "A",
        "Annual Salary Amount": 85000}

#Now I am assigning all the employees
employees = [emp1,emp2, emp3, emp4]


#Functions
#Here I create a Menu for the user where user have an option to choose the number and it get the result related to the describtion
def display_menu():
    print("\nType 1 to view the list of employees")
    print("Type 2 to Add an employee")
    print("Type 3 to Print a payslip")
    print("Type 4 to Print all payslips")
    print("Type 5 to Show annual payroll total")
    print("Type 6 to Show monthly payroll total")
    print("Type 7 to Show weekly payroll total")
    print("Type h to Help")
    print("Type 0 for Exit")

#Here I declare the function which allows user to view the employees information 
def view_employees():
    num = 1 
    for emp in employees:
        name = f'{num} {emp["First Name"]} {emp["Last Name"]}' 
        print(f'Employee: {name} \tPPSN: {emp["PPSN"]}\
              \tSalary: €{emp["Annual Salary Amount"]}')
        num +=1
#Here I declare the function which allows user to add new employees information 
def add_employee(details):
   f_name, l_name, pps, credits, prsi,sal = details

   print(f'{f_name} {l_name} {pps} {credits} {prsi} {sal}')

   new_emp = {"First Name": f_name, "Last Name": l_name, "PPSN": pps,
        "Personal Tax Credit": credits, "PRSI Class": prsi,
        "Annual Salary Amount": sal}
   employees.append(new_emp)
   view_employees()

    # newemp = dict()
    # newemp["fname"] = input("Add employee first name:").strip().capitalize()
    # newemp["lname"] = input("Add employee last name:").strip().capitalize()
    # newemp["ppsn"] = input("Add employee PPSN:")
    # newemp["Personal Tax Credit"] = input("Add employee tax_credit:")
    # newemp["PRSI Class"] =  input("Add employee PRSI class:")
    # newemp["Annual Salary Amount"] = int(input("Add employee Salary:"))

    # employees.append(newemp)

#Here I declare the function which allows user to add new employees detail and check is it valid details or not   
def employee_details():
    first_name  =""
    last_name = ""
    ppsn=""
    tax_credit =0
    salary =0
    while True: #Keep asking for a value until we are happy it is valid
        first_name = input(BLUE + "Please Enter employee First Name: " + RESET).strip().capitalize() #capitalize first letter of the name
        #The length of the name should be more than and equal 2 letter
        if len(first_name) >= 2:
            print(first_name)
            break #break out of the loop
        else:
            print(RED + "Invalid Entry!" + RESET)
    
    while True: #Keep asking for a value until we are happy it is valid
        last_name = input(BLUE + "Please Enter employee Last Name: " + RESET).strip().capitalize() #capitalize first letter of the name
        #The length of the name should be more than and equal 2 letter
        if len(last_name) >= 2:
            print(last_name)
            break #break out of the loop
        else:
            print(RED + "Invalid Entry!" + RESET)

    #PPSN should be 8 or 9 characters long.
    #The first 7 characters must be numbers and the last 1 or 2, must be letters only

    while True:
        ppsn = input(BLUE + "Add employee PPSN: " + RESET).strip()
        if len(ppsn) == 8 and ppsn[:7].isdigit() and ppsn[-1].isalpha():
            break
        elif len(ppsn) == 9 and ppsn[:7].isdigit() and ppsn[-2:].isalpha():
            break
        else:
            print(RED + "Invalid entry! PPSN should be 7 digits followed by either 1 or 2 letters." + RESET)
    #Tax_credit should be numbers        
    while True:
        tax_credit_string = input(BLUE + "Add employee Tax_Credit: " + RESET).strip()
       
        arr = tax_credit_string.split(".")
        arr_count = len(arr)
        if arr_count < 3:
            if "." in tax_credit_string and len(tax_credit_string) > 1:
                tax_credit = float(tax_credit_string)
                break
            elif tax_credit_string.isnumeric():
                tax_credit = int(tax_credit_string)
                break
            else:
                print(RED + "Invalid Entry, Tax_Credit must be number value!" + RESET)
        else:
            print(RED + "Invalid entry, Tax_Credit must contain no more than 1 decimal point!" + RESET)
     #PRSI Class should have Letter A in it and atleast two character long    
    while True:
        prsi_class = input(BLUE + "Add employee PRSI class: " + RESET)
        if len(prsi_class) == 2 and prsi_class[:1] == "A":
            print(prsi_class)
            break
        else:
            print(RED + "Invlaid Entry, PRSI_Class must begin with 'A' and be 2 characters in length!" + RESET)

    while True:
        salary_string = input(BLUE + "Add employee Annual Salary: " + RESET).strip()

        arr = salary_string.split(".")
        arr_count = len(arr)
        if arr_count < 3:
            if "." in salary_string and len(salary_string) > 1:
                salary = float(salary_string)
                break
            elif salary_string.isnumeric():
                salary = int(salary_string)
                break
            else:
                print(RED + "Invalid Entry, Salary must be number value!" + RESET)
        else:
            print(RED + "Invalid entry, Salary must contain no more than 1 decimal point!" + RESET)       

    #print(f'{first_name} {last_name} {ppsn} {tax_credit} {prsi_class} {salary}')
    return first_name, last_name, ppsn, tax_credit, prsi_class, salary

#print a payslip for a particular employee
def print_payslip(employee):
    name = f'{employee["First Name"]} {employee["Last Name"]}'
    ppsn = employee["PPSN"]
    today = datetime.date.today()
    today_formatted = today.strftime(("%d/%m/%y"))
    tax_credit = (employee["Personal Tax Credit"] + employee_tax_credit_2023) / weeks_in_2023
    prsi_classs = employee["PRSI Class"]
    salary = employee["Annual Salary Amount"]
    gross_pay = salary / weeks_in_2023
    annual_paye = get_annual_paye(employee)
    weekly_paye = annual_paye / weeks_in_2023
    ee_weekly_prsi = weekly_prsi_ee(employee)
    er_weekly_prsi = weekly_prsi_er(employee)
    yearly_usc = annual_usc(employee)
    weekly_usc =0.00
    if yearly_usc > 0:
        weekly_usc = yearly_usc /weeks_in_2023

    #Here I calculate Net Pay for the employee
    net_pay = ((gross_pay - weekly_paye) - ee_weekly_prsi) - weekly_usc

        
    print(RED + "\n****************************************************************************" + RESET)
    print(YELLOW + "\t\t\tSoft Company" + RESET)
    print(RED + "****************************************************************************" + RESET)
    print(f'Employee Name: {name} \t\tEmployee PPS No: {ppsn}')
    print(f'Date: {today_formatted}\t\t\t\tPRSI Class: {prsi_classs}')
    print(GREEN + "-----------------------------------------------------------------------------" + RESET)
    print(f'PAYE: {weekly_paye}')
    print(f'PRSI (employee): {ee_weekly_prsi}')
    print(f'PRSI (employer): {er_weekly_prsi}')
    print(f'USC: {weekly_usc}')
    print(GREEN + "-----------------------------------------------------------------------------" + RESET)
    print(f'Gross Salary: {salary / weeks_in_2023}\t\tNet Pay: {net_pay}')
    print(RED + "******************************************************************************" + RESET)

#Here I calculate Annual PAYE for the employee
def get_annual_paye(employee):
    annual_sal = employee["Annual Salary Amount"]
    high_rate_amt = 0.00
    low_rate_amt = 0.00
    tax_credit=(employee["Personal Tax Credit"]-employee_tax_credit_2023)
    tax_liability =0.00

    #If annual_sal > 40,000.00, anything above that figure is calculated at 40%
    #Everything up to that figure is calculated at 20%
    #minus tax credit
    if annual_sal > low_rate_cut_off_2023:
        #Calculate the 40% amount
        high_rate_amt = (annual_sal - low_rate_cut_off_2023) * high_rate_tax_2023
        low_rate_amt = low_rate_cut_off_2023 * low_rate_tax_2023
    else:
        low_rate_amt = annual_sal * low_rate_tax_2023

    #(20% + 40%) - credit = paye liability
    tax_liability =(high_rate_amt + low_rate_amt)- tax_credit
    return tax_liability

#Here I calculate Weekly PRSI for the employee
def weekly_prsi_ee(employee):
    prsi = 0.00
    prsi_credit = 0.00
    weekly_gross = employee["Annual Salary Amount"] / weeks_in_2023
    # If the employee is PRSI Class A and earns less than €352.01, the pay €0 
    # If they earn between €352.01 and €441 they pay 4% minus their PRSI credit.
        #Their credit is reduced by on sixth if they earn more than €352.01
    # The credit does not apply to anything over €424.01
     
    if weekly_gross < 352.01:
        prsi = 0.00
    elif weekly_gross > 352.01 and weekly_gross < 424.01:
        #1. Calculte one-sixth of your earning over €352.01. 
        prsi_credit = prsi_credit_2023 - ((weekly_gross - 352.01) /6)
        prsi = (weekly_gross * 0.04) - prsi_credit
    elif weekly_gross > 441:
        prsi = (weekly_gross * 0.04)
    return prsi

#Here I calculate Weekly PRSI for the employer
def weekly_prsi_er(employee):
    prsi = 0.00
    weekly_gross = employee["Annual Salary Amount"] / weeks_in_2023

    if weekly_gross <= 441:
        prsi = (weekly_gross * 0.088)
    else:
        prsi = (weekly_gross * 0.1105)
    return prsi
#Here I calculate USC for the employee
def annual_usc(employee):
    usc = 0.00
    annual_sal = employee["Annual Salary Amount"]

    #Excempt if you earn < €13,000
    #Otherwise:
    #Standard rates and thresholds of USC for 2023
    #Threshold for 2023     Rate
    #First €12,012          0.5%
    #Next €10,908           2%
    #Next €47,124           4.5%
    #Balance                8%

    if annual_sal <13000:
        usc = 0.00
    else:
        usc = 12012 * 0.005
        annual_sal -= 12012
        if annual_sal >= 10908:
            usc += 10908 * 0.02
            annual_sal -= 10908
        else:
            usc += annual_sal * 0.02

        if annual_sal >= 47124:
            usc += 47142 * 0.045
            annual_sal -= 47124
        else:
            usc += annual_sal * 0.045

        if annual_sal > 0:
            usc += annual_sal *0.08   
    return usc

def print_all_payslip():
   #Looping the process from print a payslip,so it will print all the employees payslip
   for emp in employees:
       name = f'{emp["First Name"]} {emp["Last Name"]}'
       ppsn = emp["PPSN"]
       today = datetime.date.today()
       today_format = today.strftime(("%d/%m/%y"))
       prsi_classs = emp["PRSI Class"]
       salary = emp["Annual Salary Amount"]
       annual_paye = get_annual_paye(emp)
       weekly_paye = annual_paye / weeks_in_2023
       gross_pay = salary / weeks_in_2023
       ee_weekly_prsi = weekly_prsi_ee(emp)
       er_weekly_prsi = weekly_prsi_er(emp)
       yearly_usc = annual_usc(emp)
       weekly_usc =0.00
       if yearly_usc > 0:
         weekly_usc = yearly_usc /weeks_in_2023
         
       #Here I calculate Net Pay for the employee
       net_pay = ((gross_pay - weekly_paye) - ee_weekly_prsi) - weekly_usc
      
       print(RED + "\n****************************************************************************" + RESET)
       print(YELLOW + "\t\t\tSoft Company" + RESET)
       print(RED + "****************************************************************************" + RESET)
       print(f'Employee Name: {name} \t\tEmployee PPS No: {ppsn}')
       print(f'Date: {today_format}\t\t\t\tPRSI Class: {prsi_classs}')
       print(GREEN + "-----------------------------------------------------------------------------" + RESET)
       print(f'PAYE: {weekly_paye}')
       print(f'PRSI (employee): {ee_weekly_prsi}')
       print(f'PRSI (employer): {er_weekly_prsi}')
       print(f'USC: {weekly_usc}')
       print(GREEN + "-----------------------------------------------------------------------------" + RESET)
       print(f'Gross Salary: {salary / weeks_in_2023}\t\tNet Pay: {net_pay}')
       print(RED + "******************************************************************************" + RESET)

#Here I calculate yearly payroll for all employees
def calc_annual_total():
    annual_total_payroll = 0
    for emp in employees:
        annual_total_payroll += emp["Annual Salary Amount"]

    print(YELLOW + "Annual Total Payroll:" + RESET, annual_total_payroll)

#Here I calculate monthly payroll for all employees
def calc_monthly_total():
    total_payroll = 0
    for emp in employees:
        total_payroll += emp["Annual Salary Amount"]
    monthly_payroll = total_payroll / 12
    print(YELLOW + "Monthly Total Payroll:"  + RESET , monthly_payroll)

#Here I calculate weekly payroll for all employees
def calc_weekly_total():
    total_payroll = 0
    for emp in employees:
        total_payroll += emp["Annual Salary Amount"]
    weekly_payroll = total_payroll / 52
    print(YELLOW + "Weekly Total Payroll:"  + RESET, weekly_payroll)

#Here I define the help and it's instruction
def help():
    print(BLUE + "\n****************************************************************" + RESET)
    print("For need help to View the list of employees you have to Type 1")
    print("For need help to Add an employee you have to Type 2")
    print("For need help to Print a payslip you have to Type 3")
    print("For need help to Print all payslips you have to Type 4")
    print("For need help to Show Annual Payroll Total you have to Type 5")
    print("For need help to Show monthly payroll total you have to Type 6")
    print("For need help to Show weekly payroll total you have to Type 7")
    print("For need help to Exit you have to Type 0")
    print(BLUE + "**********************************************************************" + RESET)

#Main Function
def main():
    while True:
        display_menu()
        option = input()

        if (option == "1"):
            view_employees()
        elif(option == "2"):
            add_employee(employee_details())
        elif(option == "3"):
            view_employees()
            #Here I unable to user to enter invalid input only numbers must be accepted.
            try:
                emp_no = int(input(BLUE + "Please provide the employee number: " + RESET))
                print_payslip(employees[emp_no -1])
            except:
                print(RED + "\nInvalid Entry, Employee number must be numeric value!" + RESET)
        
        elif(option == "4"):
            print_all_payslip()
        elif(option == "5"):
            calc_annual_total()
        elif(option == "6"):
            calc_monthly_total()
        elif(option == "7"):
            calc_weekly_total()
        elif(option == "h"):
            help()
        elif(option == "0"):
            print(RED + "Application is Exit!" + RESET)
            break
        else:
            print(RED + "Invalid Entry!, Try Again!" + RESET)   

#Call Main
main()