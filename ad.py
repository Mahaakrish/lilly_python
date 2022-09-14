d1 = {
    "apple": 280,
    "banana": 60,
    "cat": 3800,
    "dog": 20000,
    "egg": 5,
    "food": 50
}

key = input("Enter the item: ")

if(d1.__contains__(key)):
    print(d1[key])
else:
    print("No such item exist..")

