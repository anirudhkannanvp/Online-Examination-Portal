# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
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
    if(request.POST.get('topic_name', False) != False and request.POST.get('status', False) != False and request.POST.get('description', False) != False):
        temp = topic()
        temp.topic_name = request.POST['topic_name']
        temp.description = request.POST['description']
        temp.status = request.POST['status']
        if(topic.objects.filter(topic_name=temp.topic_name).count() == 0):
            temp.save()
            message = "Topic was successfully added!!"
            return render(request ,'online_exam/faculty_add_topic.html', {"message":message})
        else:
            wrong_message = "Sorry, topic already exists!!"
            return render(request ,'online_exam/faculty_add_topic.html', {"wrong_message":wrong_message})
    else:
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
    if(request.POST.get('id', False) != False and request.POST.get('topic_name', False) != False and request.POST.get('status', False) != False and request.POST.get('description', False) != False):
        temp = topic()
        temp.topic_id = request.POST['id']
        temp.topic_name = request.POST['topic_name']
        temp.description = request.POST['description']
        temp.status = request.POST['status']
        if(topic.objects.filter(topic_name=temp.topic_name).count() == 0 and topic.objects.filter(id=temp.topic_id).update(topic_name=temp.topic_name, description = temp.description, status = temp.status, modified = datetime.datetime.now())):
            message = "Topic was updated successfully!!"
            return render(request ,'online_exam/faculty_add_topic.html', {"message":message})
        else:
            wrong_message = "Sorry, the topic already exists!!"
            return render(request ,'online_exam/faculty_add_topic.html', {"wrong_message":wrong_message})
    else:
        return render(request ,'online_exam/faculty_modify_topic.html', {"topics":topic.objects.all()})

def faculty_modify_subtopic(request):
    return render(request ,'online_exam/faculty_modify_subtopic.html')

def faculty_modify_question(request):
    return render(request ,'online_exam/faculty_modify_question.html')

def faculty_update_course(request):
    return render(request ,'online_exam/faculty_update_course.html')

def faculty_update_exam(request):
    return render(request ,'online_exam/faculty_update_exam.html')

def faculty_update_topic(request):
    result = topic.objects.get(pk = int(request.POST['id']))
    return render(request ,'online_exam/faculty_update_topic.html', {"result": result})

def faculty_update_subtopic(request):
    return render(request ,'online_exam/faculty_update_subtopic.html')

def faculty_update_question(request):
    return render(request ,'online_exam/faculty_update_question.html')

def faculty_view_courses(request):
    return render(request ,'online_exam/faculty_view_courses.html', {"courses":course.objects.all()})

def faculty_view_exams(request):
    return render(request ,'online_exam/faculty_view_exams.html')

def faculty_view_topics(request):
    return render(request ,'online_exam/faculty_view_topics.html', {"topics":topic.objects.all()})

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