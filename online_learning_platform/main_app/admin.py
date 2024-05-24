from django.contrib import admin
from main_app.models import UserProfileInfo, Course, Category, Teacher, Quiz, Question
from main_app.forms import CourseForm, CategoryForm, TeacherForm
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    form=CourseForm
    raw_id_fields = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1 

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class TeacherAdmin(admin.ModelAdmin):
    form=TeacherForm

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1 

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(UserProfileInfo)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)



