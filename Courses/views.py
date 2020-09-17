from django.shortcuts import render, redirect
from .models import Course, Class, Topic, Notes
from .forms import CourseForm, ClassForm, TopicForm, NotesForm
from django.contrib.auth.decorators import login_required
from Profile.models import Profile, Teacher, Student


def Home(request):
    courses = Course.objects.all()
    
    context = {
        "courses":courses
        }
    
    return render(request, "Courses/Home.html", context)



@login_required
def Create(request, name):
    profile = Profile.objects.get(user=request.user)
    if name == "Course":
        form = CourseForm(request.POST or None)
    elif name == "Class":
        form = ClassForm(request.POST or None)
    elif name == "Topic":
        form = TopicForm(request.POST or None)
    else:
        return redirect('/')
    
    if form.is_valid():
        form.save()
        return redirect('/')
        
    context = {
        "form":form
        }
    
    return render(request, "Courses/Create.html", context)

def Class_List(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    classes = Class.objects.filter(class_course=course)
    
    
    context = {
        "course":course,
        "classes":classes,
        }
    return render(request, "Courses/ClassList.html", context)

def Topic_List(request, course_slug, class_slug):
    course = Course.objects.get(slug=course_slug)
    the_class = Class.objects.get(slug=class_slug)
    topics = Topic.objects.filter(topic_class=the_class)
    
    context = {
        "course":course,
        "class":the_class,
        "topics":topics
        }
    
    return render(request, "Courses/TopicList.html", context)

def Notes_List(request, course_slug, class_slug, topic_slug):
    course = Course.objects.get(slug=course_slug)
    the_class = Class.objects.get(slug=class_slug)
    topic = Topic.objects.get(slug=topic_slug)
    notes = Notes.objects.filter(topic_notes=topic)
    
    context = {
        "course":course,
        "class":the_class,
        "topic":topic,
        "notes":notes
        }
    
    return render(request, "Courses/NotesList.html", context)

@login_required
def Create_Notes(request, topic_slug):
    profile = Profile.objects.get(user=request.user)
    if not Teacher.objects.filter(profile=profile):
        return redirect('Course:NotTeacher')
    teacher = Teacher.objects.get(profile=profile)
    topic = Topic.objects.get(slug=topic_slug)
    if not topic.topic_class in teacher.classes.all():
        return redirect('Profile:Login')
    form = NotesForm(request.POST or None)
    
    if form.is_valid():
        form = form.cleaned_data
        author = request.user
        title = form['title']
        information = form['information']
        topic_notes = topic
        Notes.objects.create(author=author, title=title, information=information, topic_notes=topic_notes)
        return redirect('Course:Home')
    
    context = {
        "form":form
        }
    
    return render(request, "Courses/CreateNote.html", context)

@login_required
def JoinAsStudent(request):
    profile = Profile.objects.get(user=request.user)
    Student.objects.create(profile=profile)
    return redirect('Course:Home')

    
    
    
    
    
    
    
    
    
    