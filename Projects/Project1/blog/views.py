from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def profile(request):
    return HttpResponse("Profile")

def example(request):
    return HttpResponse("Hello, world. You're at the blog example.")

def student(request,student_id):
    return HttpResponse(f"Hello with the number {student_id}")

def detail(request, question_id):
    return HttpResponse(f"The id of question is {question_id}")

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

