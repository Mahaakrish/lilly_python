from datetime import date
from posixpath import split


print("\x4d")
x = date(1997,6,11)
print(x)
tod = date.today()
print(tod.year-x.year)

dob = "1997-06-11"
dob = dob.split("-")
print(dob)
