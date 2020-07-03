from django.shortcuts import render
from django.http import HttpRequest
from .models import Project,Galary
from .models import Doc
from .models import Course
from .models import Book 
# Create your views here.
def home(request):
    global projects
    global books
    global course
    projects = Project.objects.all()[:3]
    books = Book.objects.all()[:3]
    courses = Course.objects.all()[:3]
    context = {
        'projects':projects,
        'books':books,
        'courses':courses,
        
    }
    return render(request, 'portfolio/home.html', context)
def galary(request):
    galarys = Galary.objects.all()
    return render(request, 'portfolio/galary.html', {'galarys':galarys})

def project(request):
    global projects
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    return render(request, 'portfolio/projects.html', context)
def course(request):
    global course
    courses = Course.objects.all()
    context = {
        'courses':courses,
    }
    return render(request, 'portfolio/freecourse.html', context)
def book(request):
    global books
    books = Book.objects.all()
    context = {
       'books':books,
    }
    return render(request, 'portfolio/freebooks.html', context)

def document(request):
    docs = Doc.objects.all()
    return render(request, 'portfolio/documents.html', {'docs':docs} )

