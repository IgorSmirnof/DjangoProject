from django.contrib import admin
from . import models

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'category')

class CoursesInline(admin.TabularInline):
    model = models.Course
    exclude = ['created_at']
    extra = 1  #empty fields


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]
# Register your models here.

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
