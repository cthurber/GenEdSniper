import os
from bs4 import BeautifulSoup as BS

"""
Simple program to help Drew students find the courses that fulfill the maximum number of gen. ed requirements by downloading the data into a pivot table for analysis
"""

class Course(object):

    term = None
    code = None
    title = None
    professor = None
    schedule = None
    link = None
    reqs_filled = None

def get_requirement_title(webpage):
    with open(webpage,'r') as requirements_page:
        requirement_title = str(BS(requirements_page).find("title").text).strip().replace('CLA-','')
    requirements_page.close()
    return requirement_title

def get_requirement_titles(webpage_directory):
    requirement_titles = []
    for page in os.listdir(webpage_directory):
        page = webpage_directory.rstrip('/') + '/' + page
        requirement_titles.append(get_requirement_title(page))
    return requirement_titles

# Reads all Drew HTML course listing pages downloaded from Ladder into a two-dimensional dataframe returned as 'data'
# TODO Add in current term selection
def structure_listings(directory):
    data = []

    # Iterates over each HTML page in 'directory'
    for listing in os.listdir(directory):
        requirement_category = str(listing).replace('.html','')
        requirements_page = open(directory+'/'+listing,'r')

        listing_page = BS(requirements_page)
        spring_table = listing_page.find_all('table')[1]
        # NEW
        requirement_category = str(listing_page.find("title").text).replace('CLA-','').lower().strip().replace(' ','-')
        raw_rows = spring_table.find_all('tr')

        for row in raw_rows:
            data_row = [str(data.text).replace(',','::').replace('\n','').replace('\r','').strip(' ') for data in row.find_all('td')]

            # Add in requirement for Pivot Table
            data_row.append(requirement_category)
            if len(data_row) > 1: data.append(data_row)

    return data

# Given the 'directory' of desired Drew Ladder HTML, function structures and writes CSV friendly version of data to 'save_location'
def gather_listings(directory, save_location):
    data = structure_listings(directory)
    with open(save_location,'w') as selection_sheet:
        for row in data:
            row_string = ""
            for item in row:
                row_string += item + ','
            row_string.rstrip(',')
            row_string += '\n'
            print(row_string, file=selection_sheet)
        selection_sheet.close()

def gather_courses(directory, term):

    courses = {}

    full_data_path = str(directory).rstrip('/') + '/' + str(term).rstrip('/')

    for listing in structure_listings(full_data_path):

        course_code = listing[1]
        if course_code not in courses:

            course = {} #Course()

            course["term"] = listing[0]
            course["code"] = listing[1]
            course["title"] = listing[2]
            course["professor"] = listing[3]
            course["schedule"] = listing[4]
            course["link"] = listing[5]
            course["reqs_filled"] = [listing[6]]

            courses[course_code] = course
        else:
            courses[course_code]["reqs_filled"].append(listing[6])

    return courses

def is_slice_in_list(s,l):
    len_s = len(s) #so we don't recompute length of s on every iteration
    return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))

def filter_on_requirements(requirements):
    course_data = gather_courses('./raw','S2017')
    results = []
    for course in course_data:
        course_meta = course_data[course]
        all_reqs_met = True
        iteration = 0

        while all_reqs_met == True and iteration < len(requirements):
            req = requirements[iteration]
            if req not in course_meta['reqs_filled']:
                all_reqs_met = False
            iteration += 1
        if all_reqs_met == True: results.append(course_meta)
    # for course in course_data:
    #     all_reqs_met = False
    #     iteration = 0
    #     while all_reqs_met == True and iteration < len(requirements):
    #         req = requirements[iteration]
    #         course_meta = course_data[course]
    #         if req in course_meta['reqs_filled'] and all_reqs_met == True:
    #             results.append(course_meta)
    #         else:
    #             all_reqs_met = False
    #         iteration += 1
    return results
