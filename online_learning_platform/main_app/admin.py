from django.contrib import admin
from main_app.models import UserProfileInfo, Course, Category, Quiz, Question
from main_app.forms import CourseForm, CategoryForm

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1 

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(UserProfileInfo)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)