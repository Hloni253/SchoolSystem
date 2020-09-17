from django.urls import path
from .views import Home, Create, Class_List, Topic_List, Notes_List, Create_Notes, JoinAsStudent
from django.views.generic import TemplateView

app_name = "Course"
urlpatterns = [
    path("", Home, name="Home"),
    path("NotTeacher/", TemplateView.as_view(template_name="Courses/NotTeacher.html"), name="NotTeacher"),
    path("Join/Student/", JoinAsStudent, name="JoinAsStudent"),
    path("Create/<name>", Create, name="Create"),
    path("Create/Note/<topic_slug>", Create_Notes, name="CreateNote"),
    path("View/Course/<course_slug>", Class_List, name="ListClasses"),
    path("View/Course/<course_slug>/<class_slug>", Topic_List, name="ListTopics"),
    path("View/Course/<course_slug>/<class_slug>/<topic_slug>", Notes_List, name="ListNotes"),
]