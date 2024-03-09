from django.urls import path
# with the point call all files
from . import views

urlpatterns = [
    path("",views.index, name="index"), # name of routes, similitud with laravel
    #route /blog/5/ --> paramter in url
    path("<int:question_id>/",views.detail, name="results"),
    
    # route /blog/5/results
    path("<int:question_id>/results/", views.results, name="results"),
    #rote  /blog/5/vote
    path("<int:question_id>/vote/",views.vote, name="vote"),
    path("<int:student_id>/student/",views.student, name="student")
]
