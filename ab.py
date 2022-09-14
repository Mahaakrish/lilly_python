str1 = "Mahaan"

print(str1[::])

for i in str1:
    print(i.upper())

print("*"*5)

for i in range(len(str1)-1,-1,-1):
    print(str1[i].upper())