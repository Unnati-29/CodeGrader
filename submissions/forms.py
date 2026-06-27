from django import forms
from .models import Submissions


class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submissions

        fields = [
            "code",
        ]

        widgets = {
            "code": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full h-80 font-mono",
                    "placeholder": "Write your Python solution here..."
                }
            )
        }