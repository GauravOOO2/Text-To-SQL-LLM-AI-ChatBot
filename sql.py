import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

## Insert more records
cursor.execute('''Insert Into STUDENT values('John Doe','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Jane Smith','Data Science','B',88)''')
cursor.execute('''Insert Into STUDENT values('Emily Davis','AI & ML','A',90)''')
cursor.execute('''Insert Into STUDENT values('Michael Brown','AI & ML','B',85)''')
cursor.execute('''Insert Into STUDENT values('Chris Evans','DevOps','A',78)''')
cursor.execute('''Insert Into STUDENT values('Lisa Wong','DevOps','B',82)''')
cursor.execute('''Insert Into STUDENT values('Kunal Shah','Cloud Computing','A',92)''')
cursor.execute('''Insert Into STUDENT values('Sarah Lee','Cloud Computing','B',89)''')
cursor.execute('''Insert Into STUDENT values('Vikas Patel','Cybersecurity','A',80)''')
cursor.execute('''Insert Into STUDENT values('Tina Johnson','Cybersecurity','B',87)''')


## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()