#this file creates and populates the database with the course offerings (code + title)
import sqlite3
from web_scrape import main
year_lst, course_lst, stream_dict = main()

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

table_query = ''' 
CREATE TABLE IF NOT EXISTS courses(
course_code TEXT,
course_title TEXT
)
'''
#^creating a table with 2 columns: course_code, and course_title

cursor.execute(table_query)

for course in course_lst: #inserting courses into the table courses
    split = course.split(" - ") #need to split into the two columns (course_code, course_title)
    code = split[0]
    title = split[1]

    cursor.execute("INSERT INTO courses VALUES (?,?)", (code, title))
connection.commit() #save insert in db
cursor.execute("SELECT * FROM courses")

results = cursor.fetchall()
connection.close()