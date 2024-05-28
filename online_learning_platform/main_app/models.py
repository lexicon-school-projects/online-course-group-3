from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_path = models.CharField(max_length=255, default='images/art.jpg')  # Set default value here

    def __str__(self):
        return self.title

class Teacher(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    bio=models.TextField(null=True)

    def __str__(self):
        return self.last_name

class Course(models.Model):
    id=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    teacher=models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)


