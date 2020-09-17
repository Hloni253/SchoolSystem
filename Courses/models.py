from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class InheritFrom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
class Course(InheritFrom):
    def Display_Course(self):
        return reverse("Course:ListClasses", kwargs={"course_slug":self.slug})
    
class Class(InheritFrom):
    class_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name="Course")
    
    def Display_Topics(self):
        return reverse("Course:ListTopics", kwargs={"course_slug":self.class_course.slug, "class_slug":self.slug})
    

class Topic(InheritFrom):
    topic_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name="Class")
    
    def Display_Notes(self):
        return reverse("Course:ListNotes", kwargs={"course_slug":self.topic_class.class_course.slug, "class_slug":self.topic_class.slug,\
                                                   "topic_slug":self.slug})
    
class Notes(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    information = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    topic_notes = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    def Short(self):
        return self.information[:2]