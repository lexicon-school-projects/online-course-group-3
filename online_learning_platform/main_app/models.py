from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Images(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True)
    
    def __str__(self):
        return self.profile_pic.name if self.profile_pic else 'No image'


class Category(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title
    


class Teacher(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    email=models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

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


class Video(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Pdf(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank= True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline= models.DateField(blank=True)

    def __str__(self):
        return self.title