from django.db import models
from django.contrib.auth.models import User
from Courses.models import Course, Class
from django.db.models.signals import post_save
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.user.username
    

def Create_Profile_Automaticaly(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance, slug=instance)
        except:
            pass
        
post_save.connect(Create_Profile_Automaticaly, sender=User)
    
class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class, related_name="TeacherClasses", blank=True)
    
    def __str__(self):
        return self.profile.user.username

class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    classes = models.ManyToManyField(Class, related_name="StudentClasses", blank=True)
    
    def __str__(self):
        return self.profile.user.username