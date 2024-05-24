from django.contrib import admin
from main_app.models import UserProfileInfo, Course, Category, Teacher
from main_app.forms import CourseForm, CategoryForm, TeacherForm
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    form=CourseForm
    raw_id_fields = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    form=CategoryForm

class TeacherAdmin(admin.ModelAdmin):
    form=TeacherForm

admin.site.register(UserProfileInfo)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Teacher)




