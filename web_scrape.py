#this is the web scraper for https://calendar.macewan.ca/programs/degree-programs/bsc-computer-science/#studentplantext
import requests
from bs4 import BeautifulSoup

def read_site(url): 
    '''
    purpose: to read site data and store the html into a variable (uses requests library, gets info from MacEwan calendar page)
    parameters: url
    return: site_data 
    '''
    header_dict = {"Status":"Approve"}
    response = requests.get(url,headers=header_dict)

    if response.status_code == 200:
        site_data = response.text
        return site_data

    else:
        print("somethings wrong")
        return

def extract_years(dirty_data):
    '''
    purpose: helper function to extract the years from the scraped webpage data (dirty_data),
    parameters: dirty_data
    return: list 
    '''
    tempstr = ''
    years = []
    soup = BeautifulSoup(dirty_data, 'html.parser') #clean up format of dirty_data
    
    course_offerings = soup.find("table", class_ = "sc_plangrid")
    temp = course_offerings.text.strip()

    for i in range(5): #getting 'year'
        tempstr += temp[i]

    for i in range(1,5): #getting year number
            tempstr += str(i)
            years.append(tempstr) #add the year to a list
            tempstr = tempstr[:5] #reset the temp str back to 'year x'
    return years

def extract_courses(dirty_data):
    '''
    purpose: helper function to extract the available courses (Fall 2027, Winter 2028, Spring-Summer 2028) from the scraped webpage data (dirty_data)
    parameters: dirty_data
    return: list
    '''
    courses = []
    soup = BeautifulSoup(dirty_data, 'html.parser')

    course_offerings = soup.find_all("td", class_ = "codecol")
    temp = course_offerings

    for i in temp: #getting courses offered (title + number)
        course_names = i.text.replace('\xa0',' ')
        if (course_names not in courses) and (len(course_names) == 8) and (course_names[0:4] == 'CMPT'): 
            #^dont want duplicates, so only add courses not entered in the courses lst. also course names are max 8 chars, and need to start with CMPT
            courses.append(course_names)

    courses = sorted(courses)
    return courses 

def main():
    '''
    purpose: main func, runs the flow: get data > clean it > 
    parameters: None
    return: None (for now)
    '''
    webpage = "https://calendar.macewan.ca/programs/degree-programs/bsc-computer-science/#studentplantext"
    site_data = read_site(webpage) 
    years = extract_years(site_data)
    courses = extract_courses(site_data)
    print(f"years: {years}")
    print(f"courses: {courses}")

main()