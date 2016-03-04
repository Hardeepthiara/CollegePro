from django.contrib import admin
from .models import Book, Student


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass
	#list_display = ('accno')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'regno','date_of_issue')



