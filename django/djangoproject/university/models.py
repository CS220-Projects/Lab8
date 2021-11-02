import uuid

from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room_id = models.ForeignKey(Room, null=False, on_delete=models.CASCADE)

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

class Enrolled(models.Model):
    class Meta:
        unique_together = (('student_id','course_id'),)

    student_id = models.ForeignKey(Student, null=False, on_delete=models.CASCADE, related_name="enrolled_student")
    course_id = models.ForeignKey(Course, null=False, on_delete=models.CASCADE, related_name="enrolled_course")
    credit_status = models.CharField(max_length=100)