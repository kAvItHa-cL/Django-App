from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext


def index(request):
    latest_question = Question.objects.order_by('publish_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question':latest_question
    })
    return HttpResponse(template.render(context))


def detail(request, questionid):
    return HttpResponse('This is the detail view of the question %s' % questionid)


def result(request, questionid):
    return  HttpResponse('This is the result view of the question %s' % questionid)


def vote(request, questionid):
    return HttpResponse('vote for the question %s' % questionid)

