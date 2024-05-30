from django.contrib import admin
from main_app.models import UserProfileInfo, Course, Category, Teacher, Quiz, Question
from main_app.forms import CourseForm, CategoryForm, TeacherForm

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ('title', 'teacher', 'video_link', 'release_date')

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1 

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm

admin.site.register(Course, CourseAdmin)
admin.site.register(UserProfileInfo)
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
