from django.contrib import admin
from django.urls import path,include
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('main_app/', include('main_app.urls')),
    path('logout', views.user_logout, name='logout'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:category_title>/courses/', views.courses_in_category, name='courses_in_category'),
    path('quiz/<str:course_title>/', views.quiz_view, name='quiz_view'),
]
