from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, LearnGroup, Student


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(LearnGroup)
class LearnGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
