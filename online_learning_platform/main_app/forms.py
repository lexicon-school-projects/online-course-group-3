from django import forms
from django.contrib.auth.models import User
from main_app.models import Student, Category, Course, Teacher


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password',)


class TeacherForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name')


class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('profile_pic',)


class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ('title', 'description',)


class CourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ('title', 'description')
