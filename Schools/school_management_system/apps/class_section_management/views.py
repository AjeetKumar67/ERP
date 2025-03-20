from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, Section, Subject
from django.contrib import messages

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_section_management/class_list.html', {'classes': classes})

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'class_section_management/section_list.html', {'sections': sections})

def create_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        new_class = Class(name=class_name)
        new_class.save()
        messages.success(request, 'Class created successfully!')
        return redirect('class_list')
    return render(request, 'class_section_management/create_class.html')

def create_section(request):
    if request.method == 'POST':
        section_name = request.POST.get('section_name')
        class_id = request.POST.get('class_id')
        new_section = Section(name=section_name, class_id=class_id)
        new_section.save()
        messages.success(request, 'Section created successfully!')
        return redirect('section_list')
    classes = Class.objects.all()
    return render(request, 'class_section_management/create_section.html', {'classes': classes})

def allocate_subject(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        section_id = request.POST.get('section_id')
        new_subject = Subject(name=subject_name, section_id=section_id)
        new_subject.save()
        messages.success(request, 'Subject allocated successfully!')
        return redirect('section_list')
    sections = Section.objects.all()
    return render(request, 'class_section_management/allocate_subject.html', {'sections': sections})