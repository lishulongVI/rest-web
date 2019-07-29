from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, LearnGroup, Student, Course, PricePolicy, DegreeCourse


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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(PricePolicy)
class PricePolicyAdmin(admin.ModelAdmin):
    list_display = ('price', 'periods', 'content_object')


@admin.register(DegreeCourse)
class DegreeCourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
