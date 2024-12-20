from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(_('Employee Name'),
                                max_length=100)
    emp_salary = models.PositiveIntegerField(_('Employee Salary'),
                                             default = 0)

    manager_id = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="managers",

                                   null=True, blank=True)


    department = models.CharField(_('Department Name'), max_length=50, null=True, blank=True)

    age = models.PositiveIntegerField(_('Age'), default=0)


    class Meta:
        db_table = "employee"


    def __str__(self):
        return f"{self.id} --- {self.emp_name}"



class Author(models.Model):
    name = models.CharField(_('Author Name'), max_length=50)


    def __str__(self):
        return f"{self.id} --- {self.name}"

    class Meta:
        db_table = "author"



class Book(models.Model):
    name = models.CharField(_('Book Name'), max_length=50)
    authors = models.ManyToManyField(Author, related_name="author_books")


    def __str__(self):
        return f"{self.id} --- {self.name}"

    class Meta:
        db_table = "book"

