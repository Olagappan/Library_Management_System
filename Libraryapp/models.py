from django.db import models

# Create your models here.

class Course(models.Model):
    Course_Name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Course_Name}'

class Books(models.Model):
    Books_Name = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50)
    Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Books_Name}'

class Student(models.Model):
    Stud_Name = models.CharField(max_length=50)
    Stud_pass = models.CharField(max_length=50)
    Stud_Phno = models.BigIntegerField()
    Stud_Sem = models.CharField(max_length=50)
    Stud_Course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Stud_Name}'

class Issue_Book(models.Model):
    Stud_Name = models.ForeignKey(Student,on_delete=models.CASCADE)
    Book_Name = models.ForeignKey(Books,on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()



