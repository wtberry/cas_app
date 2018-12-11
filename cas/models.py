from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
## Django automatidally add primary key id, unless otherwise specified

### testing Post table  ####
class Post(models.Model):
    # now attributes in the database
    title = models.CharField(max_length=100) # title, field of char, with max length of 100
    content = models.TextField() # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now) # passing function itself, therefore no () after now
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if delete user, it'll delete all of thier posts as well, by on_delete

    def __str__(self): ## magic / special method
        return self.title

##### Classes for the CAS app #####

### Courses ###
class Course(models.Model):
    ## attr
    #course_ID = models.AutoField() #unique int values
    #professor = ### professor class
    course_name = models.CharField(max_length=50)

    def __str__(self): ## magic / special method
        return self.course_name

### Employee class to be inherited ###
class Employee(models.Model):
    ## attr
    emp_id = models.AutoField(primary_key=True) # unique int values
    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)

    class Meta:
        abstract = True;

### Professor from Employee ###
class Professor(Employee):
    courses = models.ManyToManyField(Course) # many to many to courses
    def __str__(self): ## magic / special method
        return self.lname + self.fname

### Positions for supervisor  ###
class Position(models.Model):
    position_name = models.CharField(max_length=100)
    def __str__(self): ## magic / special method
        return self.position_name


### Supervisor ###
class Supervisor(Employee):
    post = models.ForeignKey(Position, on_delete=#whatever)

    def __str__(self):
        return self.lname + self.fname
    
### super class student, to be inherited for client, tutor, and SIAs
class Student(models.Model):
    ## attr
    stu_id = models.AutoField(primary_key=True) # student ID number, primary key
    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    # whether if student is grad or undergrad student
    UNDER_GRAD = 'UG'
    GRAD = 'GD'

    under_grad = (
            (UNDER_GRAD, 'Undergraduate'),
            (GRAD, 'graduate')
            )
    schools = models.CharField(max_length=2, choices=under_grad, default=UNDER_GRAD)

    # this part's for abstraction of the student class
    class Meta:
        abstract = True

    def __str__(self):
        return self.lname + self.fname

##### Students' subclasses #####
class Tutor(Student):
    courses = model.ManyToManyField(Course) # a class that this is related, and on_delete option

class Client(Student):
    course = model.ManyToManyField(Course) # clients and courses

### Class for Session ###
class Session(models.Model):
    # attributes in the database
    start_time = models.DateTimeField(default=timezone.now)
    finish_time = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(User) # client and tutor's stu_id number from other tables
    tutor = models.ForeignKey(Tutor)
    course = models.ForeignKey(Course)## SOMETHING HERE FROM COURSE TABLE)

    professor = models.ForeignKey(Professor) # prof's emp_id







