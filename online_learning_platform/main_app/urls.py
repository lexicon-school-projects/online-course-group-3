
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
    path('teacher/', views.teachers, name='teachers'),
    path('quiz/<slug:course_title>/', views.quiz_view, name='quiz_view'), 
] 