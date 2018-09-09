from django.contrib import admin

# Register your models here.
from .models import Book,Allocate

class bookadmin(admin.ModelAdmin):
	list_display=['bid','bname','author','publisher','cost']

class allocateadmin(admin.ModelAdmin):
	list_display = ['aid','sid','allodate']


admin.site.register(Allocate,allocateadmin)
admin.site.register(Book,bookadmin)