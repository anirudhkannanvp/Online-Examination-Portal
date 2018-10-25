# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import course, user, topic, subtopic, question_type, level, exam_detail, question_bank,  option, answer, registration, result

def faculty_dashboard(request):
    return render(request ,'online_exam/faculty_dashboard.html')
    
def faculty_add_course(request):
    return render(request ,'online_exam/faculty_add_course.html')

def faculty_add_exam(request):
    return render(request ,'online_exam/faculty_add_exam.html')

def faculty_add_topic(request):
    return render(request ,'online_exam/faculty_add_topic.html')

def faculty_add_subtopic(request):
    return render(request ,'online_exam/faculty_add_subtopic.html')

def faculty_add_question(request):
    return render(request ,'online_exam/faculty_add_question.html')

def faculty_modify_course(request):
    return render(request ,'online_exam/faculty_modify_course.html')

def faculty_modify_exam(request):
    return render(request ,'online_exam/faculty_modify_exam.html')

def faculty_modify_topic(request):
    return render(request ,'online_exam/faculty_modify_topic.html')

def faculty_modify_subtopic(request):
    return render(request ,'online_exam/faculty_modify_subtopic.html')

def faculty_modify_question(request):
    return render(request ,'online_exam/faculty_modify_question.html')

def faculty_update_course(request):
    return render(request ,'online_exam/faculty_update_course.html')

def faculty_update_exam(request):
    return render(request ,'online_exam/faculty_update_exam.html')

def faculty_update_topic(request):
    return render(request ,'online_exam/faculty_update_topic.html')

def faculty_update_subtopic(request):
    return render(request ,'online_exam/faculty_update_subtopic.html')

def faculty_update_question(request):
    return render(request ,'online_exam/faculty_update_question.html')

def faculty_view_courses(request):
    return render(request ,'online_exam/faculty_view_courses.html', {"courses":course.objects.all()})

def faculty_view_exams(request):
    return render(request ,'online_exam/faculty_view_exams.html')

def faculty_view_topics(request):
    return render(request ,'online_exam/faculty_view_topics.html')

def faculty_view_subtopics(request):
    return render(request ,'online_exam/faculty_view_subtopics.html')

def faculty_view_questions(request):
    return render(request ,'online_exam/faculty_view_questions.html')

def faculty_evaluate(request):
    return render(request ,'online_exam/faculty_evaluate.html')

def faculty_exam_registrations(request):
    return render(request ,'online_exam/faculty_exam_registrations.html')

def faculty_user_registrations(request):
    return render(request ,'online_exam/faculty_user_registrations.html')

def faculty_profile(request):
    return render(request ,'online_exam/faculty_profile.html')
                           
# Create your views here.
def student_dashboard(request):
	return render(request, 'online_exam/student_dashboard.html')

def student_exams(request):
	return render(request, 'online_exam/student_exams.html')

def student_progress(request):
	return render(request, 'online_exam/student_progress.html')

def student_profile(request):
	return render(request, 'online_exam/student_profile.html')