from django import forms
from django.contrib.auth.models import User
from main_app.models import UserProfileInfo, Category, Course, Teacher, Images, Assignment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model= User
        fields = ('username', 'email', 'password',)

class TeacherForm(forms.ModelForm):
    class Meta():
        model=Teacher
        fields = ('id', 'first_name', 'last_name','bio','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)


class CategoryForm(forms.ModelForm):
    class Meta():
        model= Category
        fields = ('title','description',)

class CourseForm(forms.ModelForm):
    class Meta():
        model= Course
        fields = ('id','title','teacher', 'video_link', 'description','release_date','teacher',)


class ImagesForm(forms.ModelForm):
    class Meta():
        model=Images
        fields=('profile_pic',)

class AssignmentForm(forms.ModelForm):
    class Meta():
        model=Assignment
        fields=('title','description','deadline',)