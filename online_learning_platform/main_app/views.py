from django.shortcuts import render,redirect
from main_app.forms import UserForm, UserProfileInfoForm, TeacherForm
from .models import UserProfileInfo, Course, Category, Teacher
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'main_app/index.html')

@login_required
def profile(request):
    return render(request, 'main_app/student_profile.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def categories(request):
    categories=Category.objects.all()
    return render(request, 'main_app/categories.html', {'categories': categories})

def course_list(request):
    course_list = Course.objects.all()
    return render(request, 'main_app/course_list.html', {'courses': course_list})

def teachers(request):
    teachers=Teacher.objects.all()
    return render(request, 'main_app/teacher_page.html', {'teachers': teachers})

def course_page(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'main_app/course_page.html', {'course': course})

def courses_in_category(request, title):
    category = Category.objects.get(title=title)
    courses_in_category = Course.objects.filter(category=category)
    return render(request, 'main_app/courses_in_category.html', {'courses_in_category': courses_in_category, 'category': category})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form =UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic =request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
        return render(request, 'main_app/login.html')

    else:
        user_form =UserForm()
        profile_form = UserProfileInfoForm
    return render(request, 'main_app/registration.html',
                {'user_form':user_form,
                 'profile_form':profile_form,
                 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('categories'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'main_app/login.html', {})
    




