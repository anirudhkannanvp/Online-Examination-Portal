# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib.auth.hashers import make_password, check_password
import requests
from .models import course, user, topic, subtopic, question_type, level, exam_detail, question_bank,  option, answer, registration, result, MatchTheColumns

def faculty_dashboard(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_dashboard.html', {"num_of_users":user.objects.count(), "num_of_exams":exam_detail.objects.count(), "num_of_questions":question_bank.objects.count()})
    else:
        return redirect("../login")

@csrf_exempt
def faculty_add_course(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
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
    else:
        return redirect("../login")

@csrf_exempt
def faculty_add_exam(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        if(request.POST.get('exam_name', False) != False and request.POST.get('description', False) != False and request.POST.get('course_id', False) != False and request.POST.get('year', False) != False and request.POST.get('status', False) != False and request.POST.get('startDate', False) != False and request.POST.get('endDate', False) != False and request.POST.get('startTime', False) != False and request.POST.get('endTime', False) != False and request.POST.get('pass_percentage', False) != False and request.POST.get('no_of_questions', False) != False and request.POST.get('attempts_allowed', False) != False):
            temp = exam_detail()
            temp.exam_name = request.POST['exam_name']
            temp.description = request.POST['description']
            temp.course_id = course.objects.get(id=request.POST['course_id'])
            temp.year = request.POST['year']
            temp.status = request.POST['status']
            temp.start_time = request.POST['startDate']+" "+request.POST['startTime']
            temp.end_time = request.POST['endDate']+" "+request.POST['endTime']
            temp.pass_percentage = request.POST['pass_percentage']
            temp.no_of_questions = request.POST['no_of_questions']
            temp.attempts_allowed = request.POST['attempts_allowed']
            if(exam_detail.objects.filter(exam_name=temp.exam_name, course_id = temp.course_id, year = temp.year).count() == 0):
                temp.save()
                print("saved")
                message = "Examination was successfully added!"
                return render(request ,'online_exam/faculty_add_exam.html', {"message":message})
            else:
                wrong_message = "Sorry, exam already exists!"
                return render(request ,'online_exam/faculty_add_exam.html', {"wrong_message":wrong_message})
        else:
            print("else entered")
            return render(request ,'online_exam/faculty_add_exam.html', {"courses":course.objects.all()})
    else:
        return redirect("../login")

def faculty_add_topic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
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
    else:
        return redirect("../login")

def faculty_add_subtopic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
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
    else:
        return redirect("../login")
def faculty_add_question(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        """print(request.POST.get("question", False))
        print(request.POST.get("description", False))
        print(request.POST.get("question_type", False))
        print(request.POST.get("subtopic", False))
        print(request.POST.get("level", False))
        print(request.POST.get("exam", False))
        print(request.POST.get("score", False))
        print(request.POST.get("status", False))"""
        if(request.method == "POST" and request.POST.get("question", False) != False and request.POST.get("description", False) != False and request.POST.get("question_type", False) != False and request.POST.get("subtopic", False) != False and request.POST.get("level", False) != False and request.POST.get("exam", False) != False and request.POST.get("score", False) != False and request.POST.get("status", False) != False):
            temp = question_bank()
            temp.question =request.POST["question"] 
            temp.description = request.POST["description"]
            temp.question_type = question_type.objects.get(pk=request.POST["question_type"])
            temp.subtopic_id = subtopic.objects.get(pk = request.POST["subtopic"])
            temp.level_id = level.objects.get(pk =request.POST["level"])
            temp.exam_id = exam_detail.objects.get(pk =request.POST["exam"])
            temp.score = request.POST["score"]
            temp.status = request.POST["status"]
            if(question_bank.objects.filter(question = temp.question, subtopic_id = temp.subtopic_id).exists() == False):
                temp.save()
                question_id = question_bank.objects.get(question = temp.question, subtopic_id = temp.subtopic_id)
                #print(temp)
                #print(temp.question_type.q_type)
                if(temp.question_type.q_type == "Multiple Choice Single Answer" or temp.question_type.q_type == "Multiple Choice Multiple Answer"):
                    for i in range(1, int(request.POST["options_number"])+1):
                        new_option = option()
                        new_option.question_id = question_id
                        new_option.option_no = i
                        new_option.option_value = request.POST["option"+str(i)]
                        new_option.save()
                    if(temp.question_type.q_type == "Multiple Choice Single Answer"):
                        temp_answer = answer()
                        temp_answer.question_id = question_id
                        temp_answer.answer = request.POST['options']
                        temp_answer.save()
                    elif(temp.question_type.q_type == "Multiple Choice Multiple Answer"):
                        answers = request.POST.getlist('options[]')
                        for i in answers:
                            new_answer = answer()
                            new_answer.question_id = question_id
                            new_answer.answer = i
                            new_answer.save()
                elif(temp.question_type.q_type == "Match the Column"):
                    for i in range(1, int(request.POST["questions_number"])+1):
                        new_row = MatchTheColumns()
                        new_row.question_id = question_id
                        new_row.question = request.POST["matchQues" + str(i)]
                        new_row.answer = request.POST["matchAns" + str(i)]
                        new_row.save()
                else:
                    temp_answer = answer()
                    temp_answer.question_id = question_id
                    temp_answer.answer = request.POST['answer']
                    temp_answer.save()
                message = "Question was successfully created!!"
                return render(request ,'online_exam/faculty_add_question.html',  {"courses": course.objects.all(), "topics": topic.objects.all(), "levels": level.objects.all(), "question_type":question_type.objects.all(), "message":message})
            else:
                wrong_message = "Sorry, question already exists under the subtopic!!"
                return render(request ,'online_exam/faculty_add_question.html', {"courses": course.objects.all(), "topics": topic.objects.all(), "levels": level.objects.all(), "question_type":question_type.objects.all(), "wrong_message":wrong_message})   
        else:
            return render(request ,'online_exam/faculty_add_question.html', {"courses": course.objects.all(), "topics": topic.objects.all(), "levels": level.objects.all(), "question_type":question_type.objects.all()})
    else:
        return redirect("../login")

@csrf_exempt
def faculty_modify_course(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        if request.method=="POST":
            temp = course()
            temp.course_id = request.POST['id']
            temp.course_name = request.POST['course_name']
            temp.description = request.POST['description']
            temp.faculty = request.POST['faculty']
            temp.status = request.POST['status']
            if(course.objects.filter(course_name=temp.course_name).count() == 0 ):
                course.objects.filter(id=temp.course_id).update(course_name=temp.course_name, description = temp.description, status = temp.status, modified = datetime.datetime.now())
                message = "Course was updated successfully!!"
                return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all(),"message":message})
            elif(course.objects.filter(course_name = temp.course_name).count() == 1 and list(course.objects.filter(course_name=temp.course_name).values("id"))[0]['id'] == int(request.POST['id'])):
                course.objects.filter(id=temp.course_id).update(course_name=temp.course_name, description = temp.description, faculty=temp.faculty, status = temp.status, modified = datetime.datetime.now())
                message = "Course was updated successfully!!"
                return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all(),"message":message})
            else:
                wrong_message = "Sorry, the course already exists!!"
                return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all(),"wrong_message":wrong_message})
        else:
            return render(request ,'online_exam/faculty_modify_course.html', {"courses":course.objects.all()})
    else:
        return redirect("../login")

@csrf_exempt
def faculty_modify_exam(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        print("entered")
        print("id---------------------------------------------------------", request.POST.get('id'))
        if(request.POST.get('id', False) != False and request.POST.get('exam_name', False) != False and request.POST.get('exam_name', False) != False and request.POST.get('description', False) != False and request.POST.get('course_id', False) != False and request.POST.get('year', False) != False and request.POST.get('status', False) != False and request.POST.get('startDate', False) != False and request.POST.get('endDate', False) != False and request.POST.get('startTime', False) != False and request.POST.get('endTime', False) != False and request.POST.get('pass_percentage', False) != False and request.POST.get('no_of_questions', False) != False and request.POST.get('attempts_allowed', False) != False):
            #if request.method == 'POST':
            temp = exam_detail()
            print("if entered")
            temp.id = request.POST['id']
            temp.exam_name = request.POST['exam_name']
            temp.description = request.POST['description']
            temp.course_id = course.objects.get(pk=request.POST['course_id'])
            temp.year = request.POST['year']
            temp.status = request.POST['status']
            temp.start_time = request.POST['startDate']+" "+request.POST['startTime']
            temp.end_time = request.POST['endDate']+" "+request.POST['endTime']
            temp.pass_percentage = request.POST['pass_percentage']
            temp.no_of_questions = request.POST['no_of_questions']
            temp.attempts_allowed = request.POST['attempts_allowed']
            if(exam_detail.objects.filter(exam_name=temp.exam_name, course_id = temp.course_id, year = temp.year).count() == 0):
                exam_detail.objects.filter(id=temp.id).update(exam_name=temp.exam_name, description=temp.description, course_id=temp.course_id, year=temp.year, status=temp.status, start_time=temp.start_time, end_time=temp.end_time, pass_percentage=temp.pass_percentage, no_of_questions=temp.no_of_questions, attempts_allowed=temp.attempts_allowed, modified=datetime.datetime.now())
                message = "Examination was successfully updated!"
                return render(request ,'online_exam/faculty_modify_exam.html', {"message":message, "exams": exam_detail.objects.all()})
            elif(exam_detail.objects.filter(exam_name=temp.exam_name, course_id = temp.course_id, year = temp.year).count() == 1 and list(exam_detail.objects.filter(exam_name=temp.exam_name, course_id = temp.course_id, year = temp.year).values("id"))[0]['id'] == int(request.POST['id'])):
                exam_detail.objects.filter(id=temp.id).update(exam_name=temp.exam_name, description=temp.description, course_id=temp.course_id, year=temp.year, status=temp.status, start_time=temp.start_time, end_time=temp.end_time, pass_percentage=temp.pass_percentage, no_of_questions=temp.no_of_questions, attempts_allowed=temp.attempts_allowed, modified=datetime.datetime.now())
                message = "Examination was successfully updated!"
            else:
                wrong_message = "Sorry, exam already exists!"
                return render(request ,'online_exam/faculty_modify_exam.html', {"wrong_message":wrong_message, "exams": exam_detail.objects.all()})
        else:
            print("else entered")
            return render(request ,'online_exam/faculty_modify_exam.html', {"exams":exam_detail.objects.all()})
    else:
        return redirect("../login")
def faculty_modify_topic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
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
    else:
        return redirect("../login")

def faculty_modify_subtopic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
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
    else:
        return redirect("../login")

def faculty_modify_question(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        Final = dict()
        if(request.method == "POST" and request.POST.get("id", False) != False and request.POST.get("question", False) != False and request.POST.get("description", False) != False and request.POST.get("question_type", False) != False and request.POST.get("subtopic", False) != False and request.POST.get("level", False) != False and request.POST.get("exam", False) != False and request.POST.get("score", False) != False and request.POST.get("status", False) != False):
            temp = question_bank()
            id = request.POST["id"]
            temp.question =request.POST["question"] 
            temp.description = request.POST["description"]
            temp.question_type = question_type.objects.get(pk=request.POST["question_type"])
            temp.subtopic_id = subtopic.objects.get(pk = request.POST["subtopic"])
            temp.level_id = level.objects.get(pk =request.POST["level"])
            temp.exam_id = exam_detail.objects.get(pk =request.POST["exam"])
            temp.score = request.POST["score"]
            temp.status = request.POST["status"]
            if(question_bank.objects.filter(question = temp.question, subtopic_id = temp.subtopic_id).exists() == False or (question_bank.objects.filter(question = temp.question, subtopic_id = temp.subtopic_id).count() == 1 and question_bank.objects.get(question = temp.question, subtopic_id = temp.subtopic_id).id == int(request.POST['id']))):
                question_bank.objects.filter(pk = int(request.POST["id"])).update(question = temp.question, description = temp.description, question_type = temp.question_type, subtopic_id = temp.subtopic_id, level_id = temp.level_id, exam_id = temp.exam_id, score = temp.score, status = temp.status, modified = datetime.datetime.now())
                question_id = question_bank.objects.get(id = int(request.POST["id"]))
                if(temp.question_type.q_type == "Multiple Choice Single Answer" or temp.question_type.q_type == "Multiple Choice Multiple Answer"):
                    option.objects.filter(question_id=question_id).delete()
                    answer.objects.filter(question_id=question_id).delete()
                    for i in range(1, int(request.POST["options_number"])+1):
                        new_option = option()
                        new_option.question_id = question_id
                        new_option.option_no = i
                        new_option.option_value = request.POST["option"+str(i)]
                        new_option.save()
                    if(temp.question_type.q_type == "Multiple Choice Single Answer"):
                        temp_answer = answer()
                        temp_answer.question_id = question_id
                        temp_answer.answer = request.POST['options']
                        temp_answer.save()
                    elif(temp.question_type.q_type == "Multiple Choice Multiple Answer"):
                        answers = request.POST.getlist('options[]')
                        for i in answers:
                            new_answer = answer()
                            new_answer.question_id = question_id
                            new_answer.answer = i
                            new_answer.save()
                elif(temp.question_type.q_type == "Match the Column"):
                    MatchTheColumns.objects.filter(question_id=question_id).delete()
                    for i in range(1, int(request.POST["questions_number"])+1):
                        new_row = MatchTheColumns()
                        new_row.question_id = question_id
                        new_row.question = request.POST["matchQues" + str(i)]
                        new_row.answer = request.POST["matchAns" + str(i)]
                        new_row.save()
                else:
                    answer.objects.filter(question_id = question_id).update(answer = request.POST['answer'])
                message = "Question was successfully modified!!"
                Final = {"message":message}
            else:
                wrong_message = "Sorry, question already exists under the subtopic!!"
                Final = {"wrong_message":wrong_message}
        V=[]
        for i in question_bank.objects.all():
            A = dict()
            A['id'] = i.id
            A['question'] = i.question
            A['description'] = i.description
            A['question_type'] = i.question_type.q_type
            A['subtopic'] = i.subtopic_id.subtopic_name
            if(A['question_type']  == "Multiple Choice Single Answer" or A['question_type'] == "Multiple Choice Multiple Answer"):
                options = ""
                for j in option.objects.filter(question_id = i).all():
                    options += (j.option_value + "; ")
                A['options'] = options
                answers = ""
                for j in answer.objects.filter(question_id = i).all():
                    answers += (option.objects.get(question_id = i, option_no=j.answer).option_value + "; ")
                A['answers'] = answers
            elif(A['question_type'] == "Match the Column"):
                A['options'] = "None"
                A['answers'] = ""
                for j in MatchTheColumns.objects.filter(question_id = i).all():
                    A['answers'] += j.question + " - " + j.answer + "; "
            else:
                A['options'] = "None"
                solution = answer.objects.get(question_id = i)
                A['answers'] = solution.answer
            A['level'] = i.level_id.level_name
            A['exam'] = i.exam_id.exam_name
            A['score'] = i.score
            A['created'] = i.created
            A['modified'] = i.modified
            A['status'] = i.status
            A['topic_name'] = (i.subtopic_id.topic_id.topic_name)
            V.append(A)
            Final["questions"] = V
        return render(request ,'online_exam/faculty_modify_question.html', Final)
    else:
        return redirect("../login")

@csrf_exempt
def faculty_update_course(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        if request.method=="POST":
            ID = request.POST['id']
            print(ID)
            data = course.objects.get(pk = int(request.POST['id']))
            return render(request ,'online_exam/faculty_update_course.html', {"data": data})
    else:
        return redirect("../login")

@csrf_exempt
def faculty_update_exam(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        result = exam_detail.objects.get(pk= int(request.POST['id']))
        start_date = ((str(result.start_time).split())[0])
        end_date = ((str(result.end_time).split())[0])
        start_time = ((str(result.start_time).split())[1]).split("+")[0]
        end_time = ((str(result.end_time).split())[1]).split("+")[0]
        return render(request ,'online_exam/faculty_update_exam.html', {"result": result, "courses": course.objects.all(), "start_date":start_date, "end_date":end_date, "start_time":start_time, "end_time":end_time})
        #print("id---------------------------------------------------------", int(request.POST['id']))
    else:
        return redirect("../login")

def faculty_update_topic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        result = topic.objects.get(pk = int(request.POST['id']))
        return render(request ,'online_exam/faculty_update_topic.html', {"result": result})
    else:
        return redirect("../login")

def faculty_update_subtopic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        result = subtopic.objects.get(pk = int(request.POST['id']))
        print(result.topic_id.topic_name)
        return render(request ,'online_exam/faculty_update_subtopic.html', {"result":result, "topics":topic.objects.all()})
    else:
        return redirect("../login")

def faculty_update_question(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        if(request.method == "POST" and request.POST.get('id', False) != False):
            query = question_bank.objects.get(pk = int(request.POST['id']))
            ques = dict()
            ques['id'] = query.id
            ques['question'] = query.question
            ques['description'] = query.description
            ques['question_type'] = query.question_type.q_type
            ques['subtopic'] = query.subtopic_id.id
            ques['topic'] = query.subtopic_id.topic_id.id
            ques['numbers'] = range(2, 11)
            if(ques['question_type']  == "Multiple Choice Single Answer" or ques['question_type'] == "Multiple Choice Multiple Answer"):
                ques['options'] = []
                for i in option.objects.filter(question_id = query).all():
                    if answer.objects.filter(question_id = query, answer = i.option_no).count() == 1:
                        ques['options'].append({"option_desig":chr(i.option_no+96), "option_no":i.option_no, "option_value":i.option_value, "answer": 1})
                    elif answer.objects.filter(question_id = query, answer = i.option_no).count() == 0:
                        ques['options'].append({"option_desig":chr(i.option_no+96), "option_no":i.option_no, "option_value":i.option_value, "answer": 0})               
                ques['options_number'] = option.objects.filter(question_id = query).count()
            elif(ques['question_type'] == "Match the Column"):
                ques['answers'] = []
                j = 1
                for i in MatchTheColumns.objects.filter(question_id = query).all():
                    ques['answers'].append({"ques_no": chr(96+j), "ques_value":i.question, "ans_no": j, "ans_value":i.answer})
                    j += 1
                ques['questions_number'] = MatchTheColumns.objects.filter(question_id = query).count()
            else:
                solution = answer.objects.get(question_id = query)
                ques['answers'] = solution.answer
            ques['level'] = query.level_id.id
            ques['exam'] = query.exam_id.id
            ques['course'] = query.exam_id.course_id.id
            ques['score'] = query.score
            ques['created'] = query.created
            ques['modified'] = query.modified
            ques['status'] = query.status
            ques['courses'] = course.objects.all()
            ques['exams'] = exam_detail.objects.filter(course_id=query.exam_id.course_id).all()
            ques['subtopics'] = subtopic.objects.filter(topic_id=query.subtopic_id.topic_id).all()
            ques['topics'] = topic.objects.all()
            ques['question_types'] = question_type.objects.all()
            ques['levels'] = level.objects.all()
        return render(request ,'online_exam/faculty_update_question.html', ques)
    else:
        return redirect("../login")

def faculty_view_courses(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_view_courses.html', {"courses":course.objects.all()})
    else:
        return redirect("../login")

@csrf_exempt
def faculty_view_exams(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        data = exam_detail.objects.all()
        #print(data)
        return render(request ,'online_exam/faculty_view_exams.html', {"exams":exam_detail.objects.all()})
    else:
        return redirect("../login")

def faculty_view_topics(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_view_topics.html', {"topics":topic.objects.all()})
    else:
        return redirect("../login")

def faculty_view_subtopics(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
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
    else:
        return redirect("../login")

def faculty_view_questions(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        V=[]
        for i in question_bank.objects.all():
            A = dict()
            A['question'] = i.question
            A['description'] = i.description
            A['question_type'] = i.question_type.q_type
            A['subtopic'] = i.subtopic_id.subtopic_name
            if(A['question_type']  == "Multiple Choice Single Answer" or A['question_type'] == "Multiple Choice Multiple Answer"):
                options = ""
                for j in option.objects.filter(question_id = i).all():
                    options += (j.option_value + "; ")
                A['options'] = options
                answers = ""
                for j in answer.objects.filter(question_id = i).all():
                    answers += (option.objects.get(question_id = i, option_no=j.answer).option_value + "; ")
                A['answers'] = answers
            elif(A['question_type'] == "Match the Column"):
                A['options'] = "None"
                A['answers'] = ""
                for j in MatchTheColumns.objects.filter(question_id = i).all():
                    A['answers'] += j.question + " - " + j.answer + "; "
            else:
                A['options'] = "None" 
                A['answers'] = answer.objects.get(question_id = i).answer
            A['level'] = i.level_id.level_name
            A['exam'] = i.exam_id.exam_name
            A['score'] = i.score
            A['created'] = i.created
            A['modified'] = i.modified
            A['status'] = i.status
            A['topic_name'] = (i.subtopic_id.topic_id.topic_name)
            V.append(A)
        return render(request ,'online_exam/faculty_view_questions.html',{"questions":V})
    else:
        return redirect("../login")

def faculty_evaluate(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_evaluate.html')
    else:
        return redirect("../login")

def faculty_exam_registrations(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_exam_registrations.html')
    else:
        return redirect("../login")

def faculty_user_registrations(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_user_registrations.html')
    else:
        return redirect("../login")

def faculty_profile(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0):
        return render(request ,'online_exam/faculty_profile.html')
    else:
        return redirect("../login")
# Create your views here.
def student_dashboard(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 1):
        return render(request, 'online_exam/student_dashboard.html')
    else:
        return redirect("../login")

def student_exams(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 1):
        return render(request, 'online_exam/student_exams.html', {"exams": exam_detail.objects.all()})
    else:
        return redirect("../login")

def student_attempt_exam(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 1):
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
    else:
        return redirect("../login")

def student_verify(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 1):
        return HttpResponse("HELLO")
    else:
        return redirect("../login")

def student_progress(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 1):
        return render(request, 'online_exam/student_progress.html')
    else:
        return redirect("../login")

def student_profile(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 1):
        return render(request, 'online_exam/student_profile.html')
    else:
        return redirect("../login")

def login(request):
    if(request.session.get('id', False) == False):
        if(request.method == "POST" and request.POST.get('email', False) != False and request.POST.get('password', False) != False):
            if(user.objects.filter(email = request.POST['email']).exists()):
                login_user = user.objects.get(email = request.POST['email'])
                if (check_password(request.POST.get('password', False),login_user.password) == True):
                    request.session['id'] = login_user.id
                    request.session['first_name'] = login_user.first_name
                    request.session['last_name'] = login_user.last_name
                    request.session['email'] = login_user.email
                    request.session['phone'] = login_user.phone
                    request.session['account_type'] = login_user.account_type
                    return redirect('../login')
                else:
                    return render(request, 'online_exam/Login.html', {"message":"Invalid Credentials!!"})
            else:
                return render(request, 'online_exam/Login.html', {"message":"Invalid Credentials!!"})
        return render(request, 'online_exam/Login.html')
    elif(request.session.get('account_type', False) == 0):
        return redirect("../faculty_dashboard")
    elif(request.session.get('account_type', False) == 1):
        return redirect("../student_dashboard")
    return render(request, 'online_exam/Login.html')

def signup(request):
    if(request.method == "POST" and request.POST.get('first_name', False) != False and request.POST.get('last_name', False) != False and request.POST.get('email', False) != False and request.POST.get('phone', False) != False):
        new_user = user(first_name = request.POST['first_name'], last_name = request.POST['last_name'], phone = request.POST['phone'], email = request.POST['email'], password = make_password(request.POST['password']))
        if(user.objects.filter(email=request.POST['email']).exists()):
            error_message = "Email ID already exists!!"
            return render(request, 'online_exam/Signup.html', {"error_message":error_message})
        else:
            new_user.save()
            message = "Account Created Successfully!!"
            return render(request, 'online_exam/Signup.html', {"message":message})
    return render(request, 'online_exam/Signup.html')

def sign_out(request):
    request.session.flush()
    return redirect('../login')

def authenticate(request, token=None):
    clientSecret = "1c616e2f378f9aa90c936b1560e6d0c372fa5e5a54457356f39573955e7e64b445d2f03673a8905088b43c114465020825f48b79e8ce85b0e20e6ad8b736e860"
    Payload = { 'token': token, 'secret': clientSecret }
    k = requests.post("https://serene-wildwood-35121.herokuapp.com/oauth/getDetails", Payload)
    data = json.loads(k.content) 
    """print(data['student'][0]['Student_Email'])
    user_email = data['student'][0]['Student_Email']
    if(user.objects.filter(email=user_email).exists() == False):
        new_user = user()
        new_user.first_name = data['student'][0]['Student_First_Name']
        new_user.last_name = data['student'][0]['Student_Last_name']
        new_user.email = data['student'][0]['Student_Email']
        new_user.phone = data['student'][0]['Student_Mobile']
        new_user.password = make_password("iamstudent")
        new_user.save()
    login_user = user.objects.get(email = user_email)
    request.session['id'] = login_user.id
    request.session['first_name'] = login_user.first_name
    request.session['last_name'] = login_user.last_name
    request.session['email'] = login_user.email
    request.session['phone'] = login_user.phone
    request.session['account_type'] = login_user.account_type"""
    print(data)
    return redirect('login')

def get_exams_by_course(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0 and request.POST.get('course_id', False) != False):
        exams = dict()
        j = 0
        for i in (exam_detail.objects.filter(course_id=course.objects.filter(id = request.POST.get('course_id', False)).all()).values("id", "exam_name")):
            exams[i['id']] = i['exam_name']
            j += 1
        return HttpResponse(json.dumps(exams))
    return HttpResponseNotFound('<h1>Page not found</h1>')

def get_subtopics_by_topic(request):
    if(request.session.get('id', False) != False and request.session.get('account_type', False) == 0 and request.POST.get('topic_id', False) != False):
        subtopics = dict()
        j = 0
        for i in (subtopic.objects.filter(topic_id=topic.objects.filter(id = request.POST.get('topic_id', False)).all()).values("id", "subtopic_name")):
            subtopics[i['id']] = i['subtopic_name']
            j += 1
        return HttpResponse(json.dumps(subtopics))
    return HttpResponseNotFound('<h1>Page not found</h1>')