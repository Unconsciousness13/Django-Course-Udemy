from django.shortcuts import render
from django.shortcuts import HttpResponse



def projects(request):
    return render(request, 'projects.html')


def project(request, pk):
    return HttpResponse('project' + ' ' + str(pk))
