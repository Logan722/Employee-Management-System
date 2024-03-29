# creating empty lists for employee name, ssn, phone, email and salary
employeeName = []
employeeSSN = []
employeePhone = []
employeeEmail = []
employeeSalary = []


def add_employee():
    # asking user how may employee data they would like to register to the database
    noe = int(input("Enter How Many Employee's Data You Would Like To Add To The Database: "))
    for i in range(noe):
        # prompting directing users to ender their information
        name = input("Enter Your Full Name: ")
        ssn = input("Enter Your Social Security Number: ")
        phone = input("Enter Your Phone Number: ")
        email = input("Enter Your Email: ")
        salary = input("Enter Your Salary: $ ")
        print("Employee Details Have Been Successfully Recorded In The Database! "
              "You are Being Redirected To The Main Menu")

        # appending inputted value to the list
        employeeName.append(name)
        employeeSSN.append(ssn)
        employeePhone.append(phone)
        employeeEmail.append(email)
        employeeSalary.append(salary)


def print_employee_by_ssn():
    ssn = input("Enter The SSN of The Employee You Would Like To Retrieve From The Database: ")
    if ssn in employeeSSN:
        index = employeeSSN.index(ssn)
        print(employeeName[index].center(30, "-"), '\n', employeeSSN[index], '\n', employeePhone[index], '\n',
              employeeEmail[index], '\n', employeeSalary[index])
        print(''.center(30, "-"))
    else:
        print("Invalid SSN!")


def edit_employee():
    while True:
        ssn = input("Enter The SSN of The Employee You Would Like To Edit: ")
        if ssn in employeeSSN:
            index = employeeSSN.index(ssn)
            choice = input("Which Employee Information Would You Like To Edit (name, ssn, phone, email, salary): ")
            if choice.lower() == 'name':
                new_name = input("Enter The New Name You Would Like To See In Place of The Existing Name:")
                employeeName[index] = new_name
                print("The Change Has Been Successfully Made! You are Being Redirected To The Main Menu")
                break
            elif choice.lower() == 'ssn':
                new_ssn = input("Enter The New SSN You Would Like To See In Place of The Existing SSN:")
                employeeSSN[index] = new_ssn
                print("The Change Has Been Successfully Made! You are Being Redirected To The Main Menu")
                break
            elif choice.lower() == 'phone':
                new_phone = input("Enter The New Phone Number You Would Like To See "
                                  "In Place of The Existing Phone Number:")
                employeePhone[index] = new_phone
                print("The Change Has Been Successfully Made! You are Being Redirected To The Main Menu")
                break
            elif choice.lower() == 'email':
                new_email = input("Enter The New Email You Would Like To See In Place of The Existing Email:")
                employeeEmail[index] = new_email
                print("The Change Has Been Successfully Made! You are Being Redirected To The Main Menu")
                break
            elif choice.lower() == 'salary':
                new_salary = input("Enter The New Salary You Would Like To See In Place of The Existing Salary:")
                employeeSalary[index] = new_salary
                print("The Change Has Been Successfully Made! You are Being Redirected To The Main Menu")
                break
            else:
                print("Invalid Detail. Kindly input any of the following options: name, ssn, phone, email or salary")
        else:
            print("SSN IS NOT IN THE DATABASE! PLEASE TRY AGAIN")


def export_to_file():
    with open('employee_info.txt', 'w') as f:
        for i in range(len(employeeName)):
            f.write(f'Employee Name: {employeeName[i]}\n')
            f.write(f'SSN: {employeeSSN[i]}\n')
            f.write(f'Phone: {employeePhone[i]}\n')
            f.write(f'Email: {employeeEmail[i]}\n')
            f.write(f'Salary: {employeeSalary[i]}\n\n')
        print("Employee information has been successfully exported to 'employee_info.txt'!")


def import_from_text_file():
    newemployeeName = []
    newemployeeSSN = []
    newemployeeEmail = []
    newemployeePhone = []
    newemployeeSalary = []

    file_path = input("Enter the file path to import: ")

    with open(file_path, 'r') as text:
        for line in text:
            line = line.strip()
            if line.startswith('Employee Name'):
                newemployeeName.append(line.split(':')[1].strip())
            elif line.startswith('SSN'):
                newemployeeSSN.append(line.split(':')[1].strip())
            elif line.startswith('Email'):
                newemployeeEmail.append(line.split(':')[1].strip())
            elif line.startswith('Phone'):
                newemployeePhone.append(line.split(':')[1].strip())
            elif line.startswith('Salary'):
                newemployeeSalary.append(line.split(':')[1].strip())
        print("File Has Been Exported Successfully!")

    return employeeName, employeeSSN, employeeEmail, employeePhone, employeeSalary


def view_employees():
    noe = len(employeeName)
    if noe > 0:
        print("There are", len(employeeName), "employees in the system.")
        choice = input("Would you like to print the values in the database [ Y / N ]:")
        if choice.upper() == 'Y':
            for i in range(noe):
                print(employeeName[i].center(30, "-"), '\n', 'SSN:', employeeSSN[i], '\n', 'Phone:', employeePhone[i],
                      '\n', 'Email:', employeeEmail[i], '\n', 'Salary:', employeeSalary[i])
                print(''.center(30, "-"))
        else:
            print("There are no employees in the database. You are being redirected to the main menu.")
    else:
        print("There are no employees in the database. You are being redirected to the main menu.")


while True:
    # prompt to ask user if they want to add new employees to the system or view present employees
    print("Employee Management System".center(60, "-"))
    print("Hello Administrator! There are", len(employeeName), "employees in the system.")
    print("".center(60, "-"))
    funct = int(input("Choose which of the following options (1 / 2 / 3 / 4 / 5 / 6) you would like to proceed with:\n"
                      "Option 1: Add Employees \n" 
                      "Option 2: View Employees In The Database \n" 
                      "Option 3: Search Employee by SSN \n"
                      "Option 4: Edit Employee Information In The Database \n" 
                      "Option 5: Export Employee's Information To A Text File \n"
                      "Option 6: Import Employee's Information From A Text File \n" "What Is Your Choice? "))

    if funct == 1:
        add_employee()
    elif funct == 2:
        view_employees()
    elif funct == 3:
        print_employee_by_ssn()
    elif funct == 4:
        edit_employee()
    elif funct == 5:
        export_to_file()
    elif funct == 6:
        employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary = import_from_text_file()
    else:
        print("Invalid Choice. Kindly input 1 / 2 / 3 / 4")
        continue
