from django.db import models


# Create your models here.
class Track(models.Model):
    track_name = models.CharField(max_length=200)

    def __str__(self):
        return self.track_name


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_age = models.IntegerField()
    Student_reg_date = models.DateTimeField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
