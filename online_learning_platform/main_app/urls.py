
from main_app import views
from django.urls import path
from django.contrib import admin

app_name='main_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:title>/courses/', views.courses_in_category, name='courses_in_category'),
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_page, name='course_page'),
    path('teacher/<int:id>/', views.teacher_page, name='teacher_page'),
    path('quiz/<slug:course_title>/', views.quiz_view, name='quiz_view'),
    path('assignment/<int:course_id>/', views.assignment_view, name='assignment_view'),
    path('profile/', views.profile, name='profile'),
    path('course/<int:course_id>/enroll/', views.add_course_to_user, name='add_course_to_user'),
] 