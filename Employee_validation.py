while True:
    fname = input("Enter your first name: ")
    if fname=="":
        print("Field cannot be empty..")
    elif fname.isalpha():
        break
    else:
        print("Enter valid name")

while True:
    lname = input("Enter your last name: ")
    if lname=="":
        print("Field cannot be empty..")
    elif lname.isalpha():
        break
    else:
        print("Enter valid name")

while True:
    phno = input("Enter your phone number: ")
    if phno.isnumeric():
        if len(phno)!=10:
            print("Must contain 10 digits.. Please enter again")
        else:
            break
    else:
        if phno=="":
            print("Field cannot be empty..")
        print("Enter valid phone number")

while True:
    age = input("Enter your age: ")
    if age.isnumeric():
        if len(age)>3:
            print("Enter valid age")
        else:
            break
    else:
        if age=="":
            print("Field cannot be empty..")
        print("Enter valid age")

while True:
    city = input("Enter your city: ")
    if city=="":
        print("Field cannot be empty..")
    else:
        break

while True:
    salary = input("Enter your salary: ")
    if salary.isnumeric():
        if float(salary)>0:
            break
        else:
            print("Enter valid salary")
    elif salary=="":
        print("Field cannot be empty..")
    
while True:
    dept = input("Enter your department: ")
    if dept=="":
        print("Field cannot be empty..")
    else:
        break

while True:
    pan = input("Enter your PAN No: ")
    if pan.isalnum():
        if len(pan)==10:
            p1 = pan[0:5]
            p2 = pan[5:9]
            p3 = pan[9]
            if p1.isalpha() and p3.isalpha() and p2.isnumeric():
                break
            else:
                print("Enter valid PAN No..")
        else:
            print("PAN must contain 9 characters.. Enter valid PAN No")
    else:
        if pan=="":
            print("Field cannot be empty..")
        print("Enter valid PAN No..")

print(f"The employee {fname,lname} of department {dept} is from {city}, age:{age}")
print(f"Ph No: {phno}")
print(f"Salary: {salary}")
print(f"PAN No: {pan}")