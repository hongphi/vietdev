'''
Created on July 26, 2011

@author: Thanh Phong
'''
from django.contrib import admin
from models import Answer, Question


class AdminQuestion(admin.ModelAdmin):
    list_display = ['title', 'content', 'date', 'author', 'tags', 'bonus']
    list_filter = ('date', 'title')
    search_fields = ('date', 'title')

class AdminAnswer(admin.ModelAdmin):
    list_display = ['question', 'content', 'date', 'author']
    list_filter = ('date', 'question')

admin.site.register(Question, AdminQuestion)
admin.site.register(Answer, AdminAnswer)
