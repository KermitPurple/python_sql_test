import mysql.connector as connector

db = connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = '12assignment'
        )
cursor = db.cursor()
# get display students and number of courses each student is taking
cursor.execute("""
        SELECT s.StudentID, s.First_Name, s.Last_Name, COUNT(ClassID) as number_of_classes
        FROM mcdonough_students s
        LEFT JOIN mcdonough_classlists l
        USING(StudentID)
        GROUP BY StudentID
        """)
result = cursor.fetchall()
for i in result:
    print(i)
