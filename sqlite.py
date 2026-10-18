#this file creates and populates the database with the year and course offerings
import sqlite3
from web_scrape import main
year_lst, course_lst, stream_dict = main()
# print(year_lst)
# print(course_lst)
# print(stream_dict['General'][4])

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

table_query = ''' 
CREATE TABLE courses (
course_code TEXT,
course_title TEXT
)
'''
#^creating a table with 2 columns: course_code, and course_title

cursor.execute(table_query)

connection.close()
