from django import forms
from qna.models import Question


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        exclude = [
            "date",
            "author",
            "likes",
            "bonus"]