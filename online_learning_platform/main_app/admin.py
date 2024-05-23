from django.contrib import admin
from main_app.models import UserProfileInfo, Course, Category
from main_app.forms import CourseForm, CategoryForm
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    form=CourseForm
class CategoryAdmin(admin.ModelAdmin):
    form=CategoryForm

admin.site.register(UserProfileInfo)
admin.site.register(Course)
admin.site.register(Category)




