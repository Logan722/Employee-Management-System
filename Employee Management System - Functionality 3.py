# creating empty lists for employee name, ssn, phone, email and salary
employeeName = []
employeeSSN = []
employeePhone = []
employeeEmail = []
employeeSalary = []


def add_employee(noe):
    for i in range(noe):
        # prompting directing users to ender their information
        name = input("Enter Your Full Name: ")
        ssn = input("Enter Your Social Security Number: ")
        phone = input("Enter Your Phone Number: ")
        email = input("Enter Your Email: ")
        salary = input("Enter Your Salary: $ ")

        # appending inputted value to the list
        employeeName.append(name)
        employeeSSN.append(ssn)
        employeePhone.append(phone)
        employeeEmail.append(email)
        employeeSalary.append(salary)


def print_employee(noe):
    while True:
        # displaying employee information
        choice = int(input("Which list do you want to print? (1, 2, 3, etc.): "))
        if choice > noe:
            print('Invalid choice. Kindly input a value above', noe)
            continue
        else:
            print(employeeName[choice - 1], ',', employeeSSN[choice - 1], ',', employeePhone[choice - 1], ',',
                  employeeEmail[choice - 1], ',', employeeSalary[choice - 1])

        # prompt asking user if they want to print an additional list containing employee information
        new = input('Would You Like to print an additional list (y / n):')
        if new == 'y':
            continue
        else:
            print('Thank you and Goodbye!')
            break


def view_employees():
    print("There are", len(employeeName), "employees in the system.")
    for i in range(len(employeeName)):
        print(employeeName[i], ',', employeeSSN[i], ',', employeePhone[i], ',',
            employeeEmail[i], ',', employeeSalary[i])

while True:
    # prompt to ask user if they want to add new employees to the system or view present employees
    funct = int(input("Choose which of the following options (1 / 2 ) you would like to proceed with:\n"
                "Option 1: Add Employees \n" "Option 2: View all Employees \n" "What Is Your Choice? "))

    if funct == 1:
        # asking user how may employee data they would like to register to the database
        noe = int(input("Enter How Many Employee's Data You Would Like To Add To The Database: \n"))
        add_employee(noe)
        print_employee(noe)
    elif funct == 2:
        view_employees()
    else:
        print("Invalid Choice. Kindly input 1 or 2")
        continue
