from django.db import models
from django.contrib.auth.models import User


# Create your models here.


"""Users"""


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user.last_name


"""Courses"""




class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey( Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class video(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class pdf(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

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

    def __str__(self):
        return self.quiz.title + '' + self.text


"""Interactions"""


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.course.title


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.username + ' ' + self.course.title

<<<<<<< Updated upstream

class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    reply = models.IntegerField()

    def __str__(self):
        return self.user.username + ' ' + self.course.title
=======
class video(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class pdf(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.title
>>>>>>> Stashed changes
