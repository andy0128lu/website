from django.shortcuts import render_to_response, get_object_or_404, render
from forum.models import Subject, Comment
from django.http import HttpResponseRedirect
from datetime import datetime


def homepage(request):
    return render(request, 'templates/homepage.html') 

def data(request):
    return render(request, 'templates/data.html') 

def tourist(request):
    return render(request, 'static/tourist2.csv')    

def index(request):
    subject_list = Subject.objects.all().order_by('date')[:]
    #return render_to_response('templates/board_index.html', {'subject_list': subject_list})
    return render(request, 'templates/board_index.html', {'subject_list': subject_list})

def writeSubject(request):
    #return render_to_response('templates/board_new.html') 
	return render(request, 'templates/board_new.html') 

def postSubject(request):
    s = Subject()
    s.title = request.POST['title']
    s.name = request.POST['name']
    s.content = request.POST['content']
    s.date = datetime.now()
    s.save()
    return HttpResponseRedirect('/%s/' % s.id)      

def readSubject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'templates/board_read.html', {'subject': subject, 'comments':subject.comment_set.all()})

def addComment(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'templates/board_reply.html', {'subject': subject}) 
    
def postComment(request, subject_id):
    s = get_object_or_404(Subject, pk=subject_id)
    c = s.comment_set.create(name=request.POST['name'], content=request.POST['content'], date=datetime.now())
    c.save()
    return HttpResponseRedirect('/%s/' % s.id) 

         
