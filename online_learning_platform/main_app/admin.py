from django.contrib import admin

# Register your models here.
from main_app.models import UserProfileInfo, Course, Category
from main_app.forms import CourseForm, CategoryForm
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    form=CourseForm

admin.site.register(UserProfileInfo)
