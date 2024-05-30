from django.contrib import admin
from django.urls import path,include
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('main_app/', include('main_app.urls')),
    path('logout', views.user_logout, name='logout'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:title>/courses/', views.courses_in_category, name='courses_in_category'),
    path('teacher/<int:id>/', views.teacher_page, name='teacher_page'),   
    path('profile/', views.profile, name='profile'),
    path('assignment/<int:course_id>/', views.assignment_view, name='assignment_view'),
    path('course/<int:course_id>/enroll/', views.add_course_to_user, name='add_course_to_user'),
    path('course/<int:course_id>/', views.course_page, name='course_page'),
]
