from django.db import models

# Create your models here.

#creating a subject model
class Subjects(models.Model):
	sub_id = models.IntegerField()
	subject = models.CharField(max_length=200)

# creating a student model
class Students(models.Model):
	student_id = models.IntegerField()
	firstname = models.CharField(max_length=150)
	lastname = models.CharField(max_length=150)
	gender = models.CharField(max_length=10)
	dob = models.DateField()
	image = models.FilePathField(path="/studentimages")

# creating the grade/assessment table 
class Grade(models.Model):
	student = models.ForeignKey(Students,on_delete=models.CASCADE)
	ca = models.IntegerField()
	exam = models.IntegerField()
	grade = models.CharField(max_length=2)
	date_added = models.DateTimeField()
	date_updated = models.DateTimeField()