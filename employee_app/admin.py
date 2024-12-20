from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_name', 'emp_salary', 'manager_id')



@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'authors_name')


    def authors_name(self, obj):
        return [e.name for e in obj.authors.all()]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


