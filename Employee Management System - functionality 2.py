# creating empty lists for employee name, ssn, phone, email and salary
employeeName = []
employeeSSN = []
employeePhone = []
employeeEmail = []
employeeSalary = []

# asking user how may employee data they would like to register to the database
noe = int(input("Enter How Many Employee's Data You Would Like To Add To The Database: \n"))

# starting a loop that will run based on the number of employee's data they want entered
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

# displaying inputted value from employees
while True:
    # displaying employee information
    choice = int(input("Which list do you want to print? (1, 2, 3, etc.): "))
    if choice > noe:
        print('Invalid choice. Kindly input a between 1 and', noe)
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
