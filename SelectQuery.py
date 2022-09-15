import mariadb

conn = mariadb.connect(
    user = "root",
    password = "rootpassword",
    host = "localhost",
    port = 3306,
    database = "employee"
)

cur = conn.cursor()
print(cur)

cur.execute("select * from employees")

for i in cur:
    print(i)