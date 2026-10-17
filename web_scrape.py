#this is the web scraper for https://calendar.macewan.ca/programs/degree-programs/bsc-computer-science/#studentplantext
import requests
from bs4 import BeautifulSoup

def read_site(name): 
    '''
    purpose: to read site data and store the html into a var (uses requests library, gets info from MacEwan calendar page)
    parameters: name
    return: site_data
    '''
    header_dict = {"Status":"Approve"}
    response = requests.get(name,headers=header_dict)

    if response.status_code == 200:
        print("pass")
        site_data = response.text
        return site_data

    else:
        print("somethings wrong")
        return


def clean_data(dirty_data):
    '''
    purpose: to clean up site info using BeautifulSoup
    parameters:
    return:
    '''
    soup = BeautifulSoup(dirty_data, 'html.parser')
    # print(soup.get_text)
    # print(f"\n water \n{soup}")

    course_offerings = soup.find_all("div", class_ = "page_content tab_content")
    print(f"course offerings: \n{course_offerings}")

def main():
    '''
    purpose: main func, runs the flow: get data > clean it > 
    parameters: None
    return: None (for now)
    '''
    url = "https://calendar.macewan.ca/programs/degree-programs/bsc-computer-science/#studentplantext"
    site = read_site(url) 
    # print(site)
    clean_data(site)


main()