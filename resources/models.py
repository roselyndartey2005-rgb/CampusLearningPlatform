from django.db import models

# Create your models here.

from django.db import models

RESOURCE_TYPES = [
    ('NOTES', 'Notes'),
    ('VIDEO', 'Video'),
    ('LINK', 'Link'),
]

class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
      return self.title
    
class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    resource_type = models.CharField(
        max_length=5,
        choices=RESOURCE_TYPES
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='resources'
    )

    def __str__(self):
          return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name


