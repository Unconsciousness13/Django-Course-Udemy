from django.shortcuts import render
from django.shortcuts import HttpResponse



def projects(request):
    return HttpResponse('Here are our products')


def project(request):
    return HttpResponse('Single Project')


def projectPlus(request, pk):
    return HttpResponse('Single Project' + ' ' + str(pk))
