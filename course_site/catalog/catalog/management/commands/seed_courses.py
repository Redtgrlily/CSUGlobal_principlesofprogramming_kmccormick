from django.core.management.base import BaseCommand
from catalog.models import Course

class Command(BaseCommand):
    help = 'Seeds the database with initial course data'

    def handle(self, *args, **options):
        data = [
            {
                "code": "CSC101", "name": "Introduction to Computer Science", "department": "CSC",
                "room": "3004", "instructor": "Haynes", "time": "8:00 a.m.",
                "book_isbn": "9780134802749", "book_title": "Introduction to Computer Science", "prerequisite": None
            },
            {
                "code": "CSC102", "name": "Python Fundamentals", "department": "CSC",
                "room": "4501", "instructor": "Alvarado", "time": "9:00 a.m.",
                "book_isbn": "9780135166307", "book_title": "Python Programming", "prerequisite": "CSC101"
            },
            {
                "code": "CSC103", "name": "Data Structures", "department": "CSC",
                "room": "6755", "instructor": "Rich", "time": "10:00 a.m.",
                "book_isbn": "9780134682335", "book_title": "Data Structures and Algorithms", "prerequisite": "CSC102"
            },
            {
                "code": "NET110", "name": "Intro to Networking", "department": "NET",
                "room": "1244", "instructor": "Burke", "time": "11:00 a.m.",
                "book_isbn": "9781119154684", "book_title": "Networking Basics", "prerequisite": None
            },
            {
                "code": "COM241", "name": "Public Speaking", "department": "COM",
                "room": "1411", "instructor": "Lee", "time": "1:00 p.m.",
                "book_isbn": "9781319058616", "book_title": "Public Speaking Essentials", "prerequisite": None
            },
            {
                "code": "CSC201", "name": "Algorithms", "department": "CSC",
                "room": "3021", "instructor": "Anderson", "time": "2:00 p.m.",
                "book_isbn": "9780262033848", "book_title": "Introduction to Algorithms", "prerequisite": "CSC103"
            },
            {
                "code": "CSC202", "name": "Clean Code Practices", "department": "CSC",
                "room": "4052", "instructor": "Nguyen", "time": "3:00 p.m.",
                "book_isbn": "9780132350884", "book_title": "Clean Code", "prerequisite": "CSC201"
            },
            {
                "code": "CSC203", "name": "Software Development Lifecycle", "department": "CSC",
                "room": "6500", "instructor": "Chen", "time": "4:00 p.m.",
                "book_isbn": "9780133594140", "book_title": "Software Engineering", "prerequisite": "CSC202"
            },
            {
                "code": "NET210", "name": "Network Security", "department": "NET",
                "room": "2205", "instructor": "Roberts", "time": "5:00 p.m.",
                "book_isbn": "9780134448237", "book_title": "Network Security Essentials", "prerequisite": "NET110"
            },
            {
                "code": "COM250", "name": "Interpersonal Communication", "department": "COM",
                "room": "1601", "instructor": "Murphy", "time": "6:00 p.m.",
                "book_isbn": "9780205890859", "book_title": "Interpersonal Communication", "prerequisite": "COM241"
            },
        ]

        for entry in data:
            course, created = Course.objects.get_or_create(code=entry["code"], defaults=entry)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added course: {entry['code']}"))
            else:
                self.stdout.write(f"Course {entry['code']} already exists. Skipping.")