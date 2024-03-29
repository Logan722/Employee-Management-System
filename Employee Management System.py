# import phonenumbers
# prompting directing users to ender their information
employeeName = input("Enter Your Full Name: ").center(30, "-")
employeeSSN = input("Enter Your Social Security Number: ")
employeePhone = input("Enter Your Phone Number: ")
employeeEmail = input("Enter Your Email: ")
employeeSalary = input("Enter Your Salary: $ ")
x = "".center(30, "-")

# displaying inputted value from employees
print(employeeName)
print("SSN: ", employeeSSN)
print("Phone: ",'({}){}-{}'.format(employeePhone[:3],employeePhone[3:6],employeePhone[6:]))
print("Email:", employeeEmail)
print("Salary: $", employeeSalary)
print(x)


