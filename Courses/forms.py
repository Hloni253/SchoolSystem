from django import forms
from .models import Course, Class, Topic, Notes

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name","slug"]
        
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ["name","slug","class_course"]
        
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name","slug","topic_class"]
        
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title","information"]