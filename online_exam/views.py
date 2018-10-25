# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import course, user, topic, subtopic, question_type, level, exam_detail, question_bank,  option, answer, registration, result

def faculty_dashboard(request):
    return render(request ,'online_exam/faculty_dashboard.html')
    
@csrf_exempt
def faculty_add_course(request):
    if request.method=="POST":
        temp = course()
        temp.course_name = request.POST['course_name']
        temp.description = request.POST['description']
        temp.faculty = request.POST['faculty']
        print(temp)
        if(course.objects.filter(course_name=temp.course_name).count() == 0):
            temp.save()
            message = "Course was successfully added!!"
            return render(request ,'online_exam/faculty_add_course.html',{"message":message})
        else:
            wrong_message = "Sorry, course already exists!!"
            return render(request,'online_exam/faculty_add_course.html',{"wrong_message":wrong_message})   
    else:
        return render(request,'online_exam/faculty_add_course.html')    
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
    if(request.POST.get('subtopic_name', False) != False and request.POST.get('status', False) != False and request.POST.get('description', False) != False and request.POST.get('topic_id', False) != False):
        temp = subtopic()
        temp.subtopic_name = request.POST['subtopic_name']
        temp.description = request.POST['description']
        temp.status = request.POST['status']
        temp.topic_id = topic.objects.get(id=request.POST['topic_id'])
        if(subtopic.objects.filter(subtopic_name=temp.subtopic_name).count() == 0):
            temp.save()
            message = "Subtopic was successfully added!!"
            return render(request ,'online_exam/faculty_add_subtopic.html',  {"topics":topic.objects.all(),"message":message})
        else:
            wrong_message = "Sorry, subtopic already exists!!"
            return render(request ,'online_exam/faculty_add_subtopic.html',  {"topics":topic.objects.all(),"wrong_message":wrong_message})
    else:
		return render(request ,'online_exam/faculty_add_subtopic.html', {"topics":topic.objects.all()})

def faculty_add_question(request):
    return render(request ,'online_exam/faculty_add_question.html')

@csrf_exempt
def faculty_modify_course(request):
    if request.method=="POST":
        temp = course()
        temp.course_id = request.POST['id']
        temp.course_name = request.POST['course_name']
        temp.description = request.POST['description']
        temp.status = request.POST['status']
        if(course.objects.filter(course_name=temp.course_name).count() == 0 ):
            course.objects.filter(id=temp.course_id).update(course_name=temp.course_name, description = temp.description, status = temp.status, modified = datetime.datetime.now())
            message = "Course was updated successfully!!"
            return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all(),"message":message})
        elif(course.objects.filter(course_name = temp.course_name).count() == 1 and list(course.objects.filter(course_name=temp.course_name).values("id"))[0]['id'] == int(request.POST['id'])):
            course.objects.filter(id=temp.course_id).update(course_name=temp.course_name, description = temp.description, status = temp.status, modified = datetime.datetime.now())
            message = "Course was updated successfully!!"
            return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all(),"message":message})
        else:
            wrong_message = "Sorry, the course already exists!!"
            return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all(),"wrong_message":wrong_message})
    else:
        return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all()})

def faculty_modify_exam(request):
    return render(request ,'online_exam/faculty_modify_exam.html')

def faculty_modify_topic(request):
    if(request.POST.get('id', False) != False and request.POST.get('topic_name', False) != False and request.POST.get('status', False) != False and request.POST.get('description', False) != False):
        temp = topic()
        temp.topic_id = request.POST['id']
        temp.topic_name = request.POST['topic_name']
        temp.description = request.POST['description']
        temp.status = request.POST['status']
        if(topic.objects.filter(topic_name=temp.topic_name).count() == 0 ):
            topic.objects.filter(id=temp.topic_id).update(topic_name=temp.topic_name, description = temp.description, status = temp.status, modified = datetime.datetime.now())
            message = "Topic was updated successfully!!"
            return render(request ,'online_exam/faculty_modify_topic.html', {"topics":topic.objects.all(),"message":message})
        elif(topic.objects.filter(topic_name = temp.topic_name).count() == 1 and list(topic.objects.filter(topic_name=temp.topic_name).values("id"))[0]['id'] == int(request.POST['id'])):
            topic.objects.filter(id=temp.topic_id).update(topic_name=temp.topic_name, description = temp.description, status = temp.status, modified = datetime.datetime.now())
            message = "Topic was updated successfully!!"
            return render(request ,'online_exam/faculty_modify_topic.html', {"topics":topic.objects.all(),"message":message})
        else:
            wrong_message = "Sorry, the topic already exists!!"
            return render(request ,'online_exam/faculty_modify_topic.html', {"topics":topic.objects.all(),"wrong_message":wrong_message})
    else:
        return render(request ,'online_exam/faculty_modify_topic.html', {"topics":topic.objects.all()})

def faculty_modify_subtopic(request):
    if(request.POST.get('id', False) != False and request.POST.get('subtopic_name', False) != False and request.POST.get('status', False) != False and request.POST.get('description', False) != False and request.POST.get('topic_id', False) != False):
        temp = subtopic()
        temp.subtopic_id = request.POST['id']
        temp.subtopic_name = request.POST['subtopic_name']
        temp.description = request.POST['description']
        temp.status = request.POST['status']
        temp.topic_id = topic.objects.get(id=request.POST['topic_id'])
        if(subtopic.objects.filter(subtopic_name=temp.subtopic_name, topic_id = temp.topic_id).count() == 0 ):
            subtopic.objects.filter(id=temp.subtopic_id).update(subtopic_name=temp.subtopic_name, description = temp.description, topic_id =temp.topic_id, status = temp.status, modified = datetime.datetime.now())
            message = "SubTopic was updated successfully!!"
            return render(request ,'online_exam/faculty_modify_subtopic.html', {"subtopics":subtopic.objects.all(),"topics":topic.objects.all(),"message":message})
        elif(subtopic.objects.filter(subtopic_name=temp.subtopic_name, topic_id = temp.topic_id).count() == 1 and list(subtopic.objects.filter(subtopic_name=temp.subtopic_name, topic_id = temp.topic_id).values("id"))[0]['id'] == int(request.POST['id'])):
            subtopic.objects.filter(id=temp.subtopic_id).update(subtopic_name=temp.subtopic_name, description = temp.description, topic_id =temp.topic_id, status = temp.status, modified = datetime.datetime.now())
            message = "SubTopic was updated successfully!!"
            return render(request ,'online_exam/faculty_modify_subtopic.html', {"subtopics":subtopic.objects.all(),"topics":topic.objects.all(),"message":message})
        else:
            wrong_message = "Sorry, the subtopic already exists!!"
            return render(request ,'online_exam/faculty_modify_subtopic.html', {"subtopics":subtopic.objects.all(),"topics":topic.objects.all(),"wrong_message":wrong_message})
    else:
        return render(request ,'online_exam/faculty_modify_subtopic.html', {"subtopics":subtopic.objects.all(),"topics":topic.objects.all()})

def faculty_modify_question(request):
    return render(request ,'online_exam/faculty_modify_question.html')

@csrf_exempt
def faculty_update_course(request):
    if request.method=="POST":
        ID = request.POST['id']
        print(ID)
        data = course.objects.get(pk = int(request.POST['id']))
        return render(request ,'online_exam/faculty_update_course.html', {"data": data})

def faculty_update_exam(request):
    return render(request ,'online_exam/faculty_update_exam.html')

def faculty_update_topic(request):
    result = topic.objects.get(pk = int(request.POST['id']))
    return render(request ,'online_exam/faculty_update_topic.html', {"result": result})

def faculty_update_subtopic(request):
    result = subtopic.objects.get(pk = int(request.POST['id']))
    print(result.topic_id.topic_name)
    return render(request ,'online_exam/faculty_update_subtopic.html', {"result":result, "topics":topic.objects.all()})

def faculty_update_question(request):
    return render(request ,'online_exam/faculty_update_question.html')

def faculty_view_courses(request):
    return render(request ,'online_exam/faculty_view_courses.html', {"courses":course.objects.all()})

def faculty_view_exams(request):
    return render(request ,'online_exam/faculty_view_exams.html')

def faculty_view_topics(request):
    return render(request ,'online_exam/faculty_view_topics.html', {"topics":topic.objects.all()})

def faculty_view_subtopics(request):
	L=[]
	for i in subtopic.objects.all():
		K = dict()
		K['subtopic_name'] = i.subtopic_name
		K['description'] = i.description
		K['created'] = i.created
		K['modified'] = i.modified
		K['status'] = i.status
		K['topic_name'] = ((i.topic_id).topic_name)
		L.append(K)
	return render(request ,'online_exam/faculty_view_subtopics.html', {"subtopics":L})

def faculty_view_questions(request):
    V=[]
    for i in question_bank.objects.all():
        A = dict()
        A['question'] = i.question
        A['description'] = i.description
        A['question_type'] = i.question_type.q_type
        A['subtopic'] = i.subtopic_id.subtopic_name
        A['level'] = i.level_id.level_name
        A['exam'] = i.exam_id.exam_name
        A['score'] = i.score
        A['created'] = i.created
        A['modified'] = i.modified
        A['status'] = i.status
        A['topic_name'] = (i.subtopic_id.topic_id.topic_name)
        V.append(A)
    return render(request ,'online_exam/faculty_view_questions.html',{"questions":V})

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

def student_attempt_exam(request):
    questions = question_bank.objects.all()
    K = dict()
    exam_id = ""
    j = 0
    for i in questions:
        L = dict()
        L['question_id'] = i.id
        L['question'] = i.question
        L['question_type'] = i.question_type.q_type
        if(i.question_type.id == 1 or i.question_type.id == 2):
            opt_dict = dict()
            for k in option.objects.filter(question_id = i.id):
                opt_dict[k.option_no] = k.option_value
            L['options'] = opt_dict
        else:
            L['options'] = ""
        #L['answer'] = dict(answer.objects.filter(question_id = i.id).values("answer"))
        L['level'] = i.level_id.level_name
        L['subtopic'] = i.subtopic_id.subtopic_name 
        L['topic'] = i.subtopic_id.topic_id.topic_name
        L['score'] = i.score
        L['exam'] = i.exam_id.exam_name
        exam_id = i.exam_id.id
        L['course'] = i.exam_id.course_id.course_name
        j += 1
        K[j] = L
    final = json.dumps(K)
    return render(request, 'online_exam/student_attempt_exam.html', {"myArray":final, "sizeMyArray":j, "exam_id":exam_id})

def student_verify(request):
    return HttpResponse("HELLO")

def student_progress(request):
	return render(request, 'online_exam/student_progress.html')

def student_profile(request):
	return render(request, 'online_exam/student_profile.html')