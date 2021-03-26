from django.shortcuts import render
from django.http import HttpResponse

from poll.form import StudentForm
from poll.models import Student
from django.shortcuts import get_list_or_404, render, redirect


def welcome(request):
    return render(request, 'poll/welcome.html')

def index(request):
    student =  get_list_or_404(Student)
    return render(request, 'poll/index.html', {'student': student})

def load_form(request):
    form = StudentForm
    return render(request, 'poll/index.html', {'form': form})

def add(request):
    form = StudentForm(request.POST)
    form.save()
    return redirect('poll/show')

def show(request):
    list = Student.objects.all()
    return render(request, 'poll/show.html', {'list': list})

def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


# Create your views here.
