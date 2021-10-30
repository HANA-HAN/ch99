from django.contrib import admin
from student.models import Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'major')
    list_filter = ('name',)
    search_fields = ('name', 'studentnum')
