from django.contrib import admin
from django.urls import path,include
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('main_app/', include('main_app.urls')),
    path('logout', views.user_logout, name='logout'),
  
]
