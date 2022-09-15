import mariadb

conn = mariadb.connect(
    user = "root",
    password = "rootpassword",
    host = "localhost",
    port = 3306,
    database = "employee"
)
conn.autocommit = True
cur = conn.cursor()

#CREATION
print("Creating table")
try:
    cur.execute("create table employees(fname varchar(30), lname varchar(30), eid varchar(10) primary key, phno bigint, age int, city varchar(20), sal float, dept varchar(10), pan varchar(15), rel varchar(5))")
    print("Table created")
except Exception as e:
    print("Table already exists")

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
    eid = input("Enter your Employee id: ")
    if eid=="":
        print("Field cannot be empty..")
    else:
        break

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
        elif int(age)<20:
            print("Age cannot be less than 20..")
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

while True:
    rel = input("Relocation required Yes/No: ")
    if rel.lower()=="yes" or rel.lower()=="no":
        break
    else:
        print("Only yes or no is taken as input.. Plese give valid answer..")


#INSERTION
#cur.execute("insert into employees value('Mahaan','Krishna','3036649',8892826045,25,'blr',82371,'ids','fbkpm3333q','no')")
#print("One row inserted...")
a = "insert into employees(fname,lname,eid,phno,age,city,sal,dept,pan,rel) value(%s,%s,%s,%d,%d,%s,%d,%s,%s,%s)"
val = (fname,lname,eid,int(phno),int(age),city,int(salary),dept,pan,rel)
print(val)
cur.execute(a,val)

print(f"The employee {fname,lname} (ID: {eid}) of department {dept} is from {city}, age:{age}")
print(f"Ph No: {phno}")
print(f"Salary: {salary}")
print(f"PAN No: {pan}")
print(f"Relocation program: {rel}")