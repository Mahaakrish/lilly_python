"""
name = input("Enter your name: ")
att = int(input("Enter the no of classes attended: "))
tot = 200

if (att/200)*100>=70:
    print(name,"is eligible to attend exam")
else:
    print(name,"is not eligible to attend exam")
"""

ename = input("Enter name of employee: ")
sal = float(input("Enter the salary: "))
expr = int(input("Enter experience in yrs: "))

if expr>=10:
    bonus = sal*0.15
    tot = sal*1.15
    print(ename,"is eligible for 15% bonus(",bonus,"), Total sal paid:",tot)
elif expr>=5:
    bonus = sal*0.1
    tot = sal*1.1
    print(ename,"is eligible for 10% bonus(",bonus,"), Total sal paid:",tot)
elif expr>=3:
    bonus = sal*0.05
    tot = sal*1.05
    print(ename,"is eligible for 5% bonus(",bonus,"), Total sal paid:",tot)
else:
    print(ename,"is not eligible for bonus")