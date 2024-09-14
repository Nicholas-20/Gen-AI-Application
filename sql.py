import sqlite3
connection=sqlite3.connect('student.db')
cursor=connection.cursor()
table_info="""
create table STUDENT (NAME VARCHAT(25),CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""
cursor.execute(table_info)

cursor.execute(''' insert into STUDENT values ('Krish','Data science','A',90)''')
cursor.execute(''' insert into STUDENT values ('Mohit','Data science','B',100)''')
cursor.execute(''' insert into STUDENT values ('Aryan','Data science','A',86)''')
cursor.execute(''' insert into STUDENT values ('Vikash','DEVOPS','A',50)''')
cursor.execute(''' insert into STUDENT values ('Dipesh','DEVOPS','B',100)''')

print("the executed values are:")

data=cursor.execute(''' Select * from STUDENT ''')
for row in data:
    print(row)

connection.commit()
connection.close()
