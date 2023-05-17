import sys
import sqlite3
import hashlib

conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Students(
   id INT PRIMARY KEY,
   name TEXT,
   surname TEXT,
   age INTEGER,
   city TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Courses(
   id INT PRIMARY KEY,
   name TEXT,
   time_start TEXT,
   time_end TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Student_courses(
   student_id INTEGER,
   course_id INTEGER,
   FOREIGN KEY (student_id)  REFERENCES Students (id),
   FOREIGN KEY (course_id)  REFERENCES Courses (id));
""")
conn.commit()

students = (1, 'Max', 'Brooks', 24, 'Spb')
student2 = (2, 'John', 'Stones', 15, 'Spb')
student3 = (3, 'Andy', 'Wings', 45, 'Manhester')
student4 = (4, 'Kate', 'Brooks', 34, 'Spb')

# cur.execute("INSERT INTO Students VALUES(?, ?, ?, ?, ?);", student4)
# conn.commit()

course1 = (1, 'python', '21.07.21', '21.08.21')
course2 = (2, 'java', '13.07.21', '16.08.21')

# cur.execute("INSERT INTO Courses VALUES(?, ?, ?, ?);", course2)
# conn.commit()

student_course1 = (1, 1)
student_course2 = (2, 1)
student_course3 = (3, 1)
student_course4 = (4, 2)

cur.execute("select * from Students where age > 30")
print(cur.fetchall())



