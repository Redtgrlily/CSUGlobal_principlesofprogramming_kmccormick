"""
Course Info Lookup Tool
Author: Kaitlyn McCormick
Description: 
    A simple, well-structured python program to retrieve course information 
    including courrse name, room number, instructor, textbook, prerequisites 
    and meeting time based on user input. 
"""

# --- Data Definitions ---
COURSE_NAMES = {
    'CSC101': 'Introduction to Computer Science',
    'CSC102': 'Python Fundamentals',
    'CSC103': 'Data Structures',
    'NET110': 'Introduction to Networking',
    'COM241': 'Public Speaking',
    'CSC201': 'Algorithms',
    'CSC202': 'Clean Code Practices',
    'CSC203': 'Software Development Lifecycles',
    'NET210': 'Network Security',
    'COM250': 'Interpersonal Communication',
    'CSC301': 'C Programming',
    'CSC302': 'Software Design Patterns',
    'CSC303': 'Code Refactoring',
    'NET310': 'Ethical Hacking with Python',
    'COM341': 'Communication Theory and Research'
}

COURSE_ROOMS = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411',
    'CSC201': '3021',
    'CSC202': '4052',
    'CSC203': '6500',
    'NET210': '2205',
    'COM250': '1601',
    'CSC301': '3200',
    'CSC302': '5202',
    'CSC303': '6455',
    'NET310': '2250',
    'COM341': '1400'
}

COURSE_INSTRUCTORS = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee',
    'CSC201': 'Anderson',
    'CSC202': 'Nguyen',
    'CSC203': 'Chen',
    'NET210': 'Roberts',
    'COM250': 'Murphy',
    'CSC301': 'Simmons',
    'CSC302': 'Yu',
    'CSC303': 'Klein',
    'NET310': 'Jordan',
    'COM341': 'Taylor'
}

COURSE_TIMES = {
    'CSC101': 'Mondays 8:00 a.m.',
    'CSC102': 'Mondays 9:00 a.m.',
    'CSC103': 'Mondays 10:00 a.m.',
    'NET110': 'Tuesdays 11:00 a.m.',
    'COM241': 'Wednesdays 1:00 p.m.',
    'CSC201': 'Mondays 1:00 p.m.',
    'CSC202': 'Mondays 2:00 p.m.',
    'CSC203': 'Mondays 3:00 p.m.',
    'NET210': 'Tuesdays 1:00 p.m.',
    'COM250': 'Wednesdays 2:00 p.m.',
    'CSC301': 'Thursdays 8:00 a.m.',
    'CSC302': 'Thursdays 9:00 a.m.',
    'CSC303': 'Thursdays 10:00 a.m.',
    'NET310': 'Tuesdays 2:30 p.m.',
    'COM341': 'Wednesdays 3:00 p.m.'
}

COURSE_BOOKS = {
    'CSC101': ('9780134802749','Introduction to Computer Science'),
    'CSC102': ('9780135166307','Python Programming'),
    'CSC103': ('9780134682335','Data Structures and Algorithms'),
    'NET110': ('9781119154684','Networking Basics'),
    'COM241': ('9781319058616','Public Speaking Essentials'),
    'CSC201': ('9780262033848','Introduction to Algorithms'),
    'CSC202': ('9780132350884','Clean Code'),
    'CSC203': ('9780133594140','Software Engineering'),
    'NET210': ('9780134448237','Network Security Essentials'),
    'COM250': ('9780205890859','Interpersonal Communication'),
    'CSC301': ('9780131103627','The C Programming Language'),
    'CSC302': ('9780201633610','Design Patterns'),
    'CSC303': ('9780132354790','Refactoring'),
    'NET310': ('9781593277505','Black Hat Python'),
    'COM341': ('9780133938876','Communication Theory')
}

COURSE_PREREQUISITES = {
    'CSC101': None,
    'CSC102': 'CSC101',
    'CSC103': 'CSC102',
    'NET110': None,
    'COM241': None,
    'CSC201': 'CSC103',
    'CSC202': 'CSC201',
    'CSC203': 'CSC202',
    'NET210': 'NET110',
    'COM250': 'COM241',
    'CSC301': 'CSC203',
    'CSC302': 'CSC301',
    'CSC303': 'CSC302',
    'NET310': 'NET210',
    'COM341': 'COM250'
}

# --- Function Definitions ---
def get_course_info(course_code):
    """
    Retrieves course information for a given course code.
    Returns a dictionary with room, instructor, and time if course exists,
    otherwise returns None.
    """
    if course_code in COURSE_NAMES:
        return {
            'Course Name': COURSE_NAMES[course_code],
            'Room': COURSE_ROOMS[course_code],
            'Instructor': COURSE_INSTRUCTORS[course_code],
            'Time': COURSE_TIMES[course_code],
            'Book ISBN': COURSE_BOOKS[course_code][0],
            'Book Title': COURSE_BOOKS[course_code][1],
            'Prerequisite': COURSE_PREREQUISITES[course_code] or "None"
        }
    return None
    
def display_course_info(course_code, info):
    """Prints formatted course information."""
    print(f"\nCourse Information for {course_code}")
    print("-" * 40)
    print(f"Course Name : {info['Course Name']}")
    print(f"Room Number : {info['Room']}")
    print(f"Instructor  : {info['Instructor']}")
    print(f"Meeting Time: {info['Time']}")
    print(f"Book ISBN   : {info['Book ISBN']}")
    print(f"Book Title  : {info['Book Title']}")
    print(f"Prerequisite: {info['Prerequisite']}")
    print("-" * 40)
    
def list_available_courses():
    """Displays all available course codes."""
    print("\nAvailable courses:")
    for code in sorted(COURSE_NAMES):
        print(f"  - {code}: {COURSE_NAMES[code]} ")
        
# -- Main Program --

def main():
    print("Welcome to the Course Info Lookup Tool")
    course_code = input("Enter a course number (i.e., CSC101): ").strip().upper()
    
    info = get_course_info(course_code)
    if info:
        display_course_info(course_code, info)
    else:
        print("\nCourse not found. Please check the course code.")
        list_available_courses()
        
if __name__ == "__main__":
    main()