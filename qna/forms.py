from django import forms
from qna.models import Question, Answer


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        exclude = [
            "date",
            "author",
            "likes",
            "bonus"]
        
class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        exclude = [
            "date",
            "author",
            "likes",
            "question"]