from django.shortcuts import render,redirect, get_object_or_404
from main_app.forms import UserForm, UserProfileInfoForm, TeacherForm, AssignmentForm
from .models import UserProfileInfo, UserCourse, Course, Assignment, Category, Teacher, Question, Quiz
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from urllib.parse import unquote
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'main_app/index.html')


@login_required
def profile(request):
    enrolled_courses = UserCourse.objects.filter(user=request.user)
    return render(request, 'main_app/profile.html', {'user': request.user, 'enrolled_courses': enrolled_courses})

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


def teacher_page(request,id):
    teacher = get_object_or_404(Teacher, id=id)
    courses_same_teacher = Course.objects.filter(teacher=teacher)
    return render(request, 'main_app/teacher_page.html', {'teacher': teacher, 'courses_same_teacher': courses_same_teacher})


# def course_page(request, course_id):
#     course = Course.objects.get(id=course_id)
#     return render(request, 'main_app/course_page.html', {'course': course})

@login_required
def add_course_to_user(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    UserCourse.objects.get_or_create(user=request.user, course=course)
    return redirect('course_page', course_id=course.id)


def course_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_enrolled = UserCourse.objects.filter(user=request.user, course=course).exists()
    url_safe_title = slugify(course.title)
    quiz_exists = Quiz.objects.filter(course=course).exists()
    assignment_exists = Assignment.objects.filter(course=course).exists()
    return render(request, 'main_app/course_page.html', {
        'course': course,
        'user_enrolled': user_enrolled,
        'quiz_exists': quiz_exists,
        'assignment_exists': assignment_exists,
        'url_safe_title': url_safe_title,
    })

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
    


def quiz_view(request, course_title):
    decoded_course_title = course_title.replace('-', ' ').lower()
    course = get_object_or_404(Course, title__iexact=decoded_course_title)
    
    quiz = get_object_or_404(Quiz, course=course)
    questions = Question.objects.filter(quiz=quiz)
    results = None

    if request.method == 'POST':
        results = []
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            is_correct = (selected_option == question.correct_option)
            results.append({
                'question': question,
                'selected_option': selected_option,
                'is_correct': is_correct,
                'correct_option': question.correct_option
            })

    return render(request, 'main_app/quiz.html', {
        'quiz': quiz,
        'questions': questions,
        'results': results,
    })

def assignment_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assignments = Assignment.objects.filter(course=course)
    return render(request, 'main_app/assignment.html', {'course': course, 'assignments': assignments})