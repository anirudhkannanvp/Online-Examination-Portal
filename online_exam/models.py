# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import pytz
from django.db import models

class course(models.Model):
    course_name = models.CharField(default = "", max_length=100)
    description = models.TextField(null="True", blank=True)
    faculty = models.CharField(default = "", max_length=100)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.id + " " + self.course_name + " " + self.description + " " + self.created + " " + self.modified

class user(models.Model):
    first_name = models.CharField(default = "", max_length = 100)
    last_name = models.CharField(default = "", max_length = 100)
    phone = models.CharField(default = "", max_length =15)
    email = models.CharField(default = "", max_length =100)
    password = models.CharField(default = "", max_length=100)
    account_type = models.IntegerField()
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.id + " " + self.first_name + " " + self.last_name + " " + self.phone + " " + self.email + " " + self.password + " " + self.account_type + " " + self.created + " " + self.modified

class level(models.Model):
    level_name = models.CharField(default = "", max_length = 100)
    def __str__(self):
        return str(self.id) + " " + str(self.level_name)
# Create your models here.

class topic(models.Model):
    topic_name = models.CharField(default = "", max_length = 100)
    description = models.TextField(null="True", blank=True)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.id + " " + self.topic_name + " " + self.description + " " + self.created + " " + self.modified
    
class subtopic(models.Model):
    subtopic_name = models.CharField(default = "", max_length = 100)
    description = models.TextField(null="True", blank=True)
    topic_id = models.ForeignKey(topic, on_delete = models.CASCADE)
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.id + " " + self.subtopic_name + " " + self.description + " " + self.topic_id + " " + self.created + " " + self.modified

class exam_detail(models.Model):
    exam_name = models.CharField(default = "", max_length = 100)
    description = models.TextField(null="True", blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    no_of_questions = models.IntegerField()
    attempts_allowed = models.IntegerField()
    pass_percentage = models.IntegerField()
    course_id = models.ForeignKey(course, on_delete = models.CASCADE)
    year = models.IntegerField()
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.id + " " + self.exam_name + " " + self.description + " " + self.start_time + " " + self.end_time + " " + self.no_of_questions + " " + self.attempts_allowed + " " + self.pass_percentage + " " + self.course_id + " " + self.year + " " + self.created + " " + self.modified

class question_type(models.Model):
    q_type = models.CharField(default = "", max_length = 100)
    def __str__(self):
        return self.qtypeid + " " + self.q_type

class question_bank(models.Model):
    question = models.TextField(null="True", blank=True)
    description = models.TextField(null="True", blank=True)
    question_type = models.ForeignKey(question_type, on_delete = models.CASCADE)
    subtopic_id = models.ForeignKey(subtopic, on_delete = models.CASCADE)
    level_id = models.ForeignKey(level, on_delete = models.CASCADE)
    exam_id = models.ForeignKey(exam_detail, on_delete =models.CASCADE)
    score = models.FloatField()
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.question + " " + self.description + " " + self.question_type + " " + self.subtopic_id + " " + self.level_id + " " + self.exam_id + " " + self.score + " " + self.created + " " + self.modified

class registration(models.Model):
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)
    exam_id = models.ForeignKey(exam_detail, on_delete = models.CASCADE)
    attempt_no = models.IntegerField()
    registered = models.IntegerField()
    view_answers  = models.IntegerField()
    answered = models.IntegerField()
    registered_time = models.DateTimeField()
    def __str__(self):
        return self.user_id + " " + self.exam_id + " " + self.attempt_no + " " + self.registered + " " + self.view_answers + " " + self.answered + " " + self.registered_time

class result(models.Model):
    registration_id = models.ForeignKey(registration, on_delete = models.CASCADE)
    question_id = models.ForeignKey(question_bank, on_delete = models.CASCADE)
    answer = models.TextField(null="True", blank=True)
    score = models.FloatField()
    verify = models.IntegerField()
    def __str__(self):  
        return self.registration_id + " " + self.question_id + " " + self.answer + " " + self.score + " " + self.verify 

class option(models.Model):
    question_id = models.ForeignKey(question_bank, on_delete=models.CASCADE)
    option_no = models.IntegerField()
    option_value = models.TextField(null="True", blank=True)
    def __str__(self):
        return self.question_id + " " + self.option_no + " " + self.option_value

class answer(models.Model):
    question_id = models.ForeignKey(question_bank, on_delete=models.CASCADE)
    answer = models.TextField(null="True", blank=True)
    def __str__(self):
        return self.question_id + " " + self.answer