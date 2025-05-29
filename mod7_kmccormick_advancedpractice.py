from dataclasses import dataclass
from typing import Optional, Dict
from enum import Enum

# --- Enums & Data Structures ---

class Department(Enum):
    CSC = "Computer Science"
    NET = "Networking"
    COM = "Communications"
    
@dataclass
class Course:
    code: str
    name: str
    department: Department
    room: str
    instructor: str
    time: str
    book_isbn: str
    book_title: str
    prerequisite: Optional[str] = None
    
# --- Repository of Courses ---

class CourseCatalog:
    def __init__(self):
        self.courses: Dict[str, Course] = self._load_courses()
        
    def _load_courses(self) -> Dict[str, Course]:
        """Simulate loading data from a data source."""
        return {
            "CSC101": Course("CSC101", "Introduction to Computer Science", Department.CSC, "3004", "Haynes", "8:00 a.m.",
                             "9780134802749", "Introduction to Computer Science"),
            "CSC102": Course("CSC102", "Python Fundamentals", Department.CSC, "4501", "Alvarado", "9:00 a.m.",
                             "9780135166307", "Python Programming", "CSC101"),
            "CSC103": Course("CSC103", "Data Structures", Department.CSC, "6755", "Rich", "10:00 a.m.",
                             "9780134682335", "Data Structures and Algorithms", "CSC102"),
            "NET110": Course("NET110", "Intro to Networking", Department.NET, "1244", "Burke", "11:00 a.m.",
                             "9781119154684", "Networking Basics"),
            "COM241": Course("COM241", "Public Speaking", Department.COM, "1411", "Lee", "1:00 p.m.",
                             "9781319058616", "Public Speaking Essentials"),
            "CSC201": Course("CSC201", "Algorithms", Department.CSC, "3021", "Anderson", "2:00 p.m.",
                             "9780262033848", "Introduction to Algorithms", "CSC103"),
            "CSC202": Course("CSC202", "Clean Code Practices", Department.CSC, "4052", "Nguyen", "3:00 p.m.",
                             "9780132350884", "Clean Code", "CSC201"),
            "CSC203": Course("CSC203", "Software Development Lifecycle", Department.CSC, "6500", "Chen", "4:00 p.m.",
                             "9780133594140", "Software Engineering", "CSC202"),
            "NET210": Course("NET210", "Network Security", Department.NET, "2205", "Roberts", "5:00 p.m.",
                             "9780134448237", "Network Security Essentials", "NET110"),
            "COM250": Course("COM250", "Interpersonal Communication", Department.COM, "1601", "Murphy", "6:00 p.m.",
                             "9780205890859", "Interpersonal Communication", "COM241"),
        }
    def get_course(self, course_code: str) -> Optional[Course]:
        return self.courses.get(course_code.upper())
    
    def list_courses(self) -> None:
        print("\nAvailable Courses:")
        for course in sorted(self.courses.values(), key=lambda c: c.code):
            print(f"  - {course.code}: {course.name}")
            
# --- Custom Exceptions ---

class CourseNotFoundError(Exception):
    def __init(self, code: str):
        super().__init__(f"Course '{code}' not found in catalog.")
        self.code = code
        
# --- Main Logic ---

def display_course_info(course: Course) -> None:
    print(f"\nCourse Information for {course.code}")
    print("-" * 45)
    print(f"Course Name   : {course.name}")
    print(f"Department    : {course.department.value}")
    print(f"Room Number   : {course.room}")
    print(f"Instructor    : {course.instructor}")
    print(f"Meeting Time  : {course.time}")
    print(f"Book ISBN     : {course.book_isbn}")
    print(f"Book Title    : {course.book_title}")
    print(f"Prerequisite  : {course.prerequisite or 'None'}")
    print("-" * 45)
    
def main():
    catalog = CourseCatalog()
    user_input = input("Enter a course number (i.e., CSC101): ").strip().upper()
    
    try:
        course = catalog.get_course(user_input)
        if not course:
            raise CourseNotFoundError(user_input)
        display_course_info(course)
    except CourseNotFoundError as e:
        print(f"\nError: {e}")
        catalog.list_courses()
        
if __name__ == "__main__":
    main()