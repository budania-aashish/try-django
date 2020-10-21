# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World! You are at poll's index page!")


def detail(request, question_id):
    return HttpResponse("You are looking at question %s. " % question_id)


def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s. " % question_id)
