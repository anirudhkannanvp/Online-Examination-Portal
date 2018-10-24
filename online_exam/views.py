# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import course, user, topic, subtopic, question_type, level, exam_detail, question_bank,  option, answer, registration, result

def home(request):
    return render(request ,'online_exam/home.html')
# Create your views here.
def student(request):
	return render(request, 'online_exam/student_home.html')
