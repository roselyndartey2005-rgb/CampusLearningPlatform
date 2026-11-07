from django.contrib import admin

from .models import Course,Resource,Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course_code')
    search_fields = ('title', 'course_code')
    list_filter = ()


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'resource_type', 'course')
    search_fields = ('title', 'description')
    list_filter = ('resource_type', 'course')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')

# Register your models here.
