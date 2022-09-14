"""
nums = (1,2,3,4)
sum = 0

for num in nums:
    sum = sum+num

print(sum)
"""


for i in range(5):
    name = input("Enter ur name: ")
    if name=="":
        print("Name cannot be empty..")
    else:
        break


for i in range(5):
    phno = input("Enter ur Ph No: ")
    if phno.isalpha():
        print("Enter valid number.. String not allowed")
    elif len(phno)!=10:
        print("Enter valid number.. 10 digits expected")
    elif phno=="":
        print("Phone number cannot be empty")
    else:
        break

age = int(input("Enter ur age: "))
if age<20:
    print("Age << 20")
    