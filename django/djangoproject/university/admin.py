from django.contrib import admin

from .models import Room, Course, Student, Enrolled
# Register your models here.

admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrolled)
