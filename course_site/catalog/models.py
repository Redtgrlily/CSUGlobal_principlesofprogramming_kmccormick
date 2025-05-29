from django.db import models

class Course(models.Model):
    DEPARTMENTS = [
        ('CSC', 'Computer Science'),
        ('NET', 'Networking'),
        ('COM', 'Communications'),
    ]
    
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=3, choices=DEPARTMENTS)
    room = models.CharField(max_length=10)
    instructor = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    book_isbn = models.CharField(max_length=20)
    book_title = models.CharField(max_length=200)
    prerequisite = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return f"{self.code}: {self.name}"