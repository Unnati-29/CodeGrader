from django import forms
from .models import Submissions

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions

        fields =[
            'student_name',
            'code'
        ]

        widgets = {
            'student_name': forms.TextInput(
                attrs={
                    'class': 'w-full p-3 rounded bg-slate-800'
                }
            ),

            'code': forms.Textarea(
                attrs={
                    'class': 'w-full p-3 rounded bg-slate-800',
                }
            )
        }
