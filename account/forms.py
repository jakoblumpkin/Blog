from django import forms
from .models import section


class commentForm(forms.ModelForm):
    class Meta:
        model=section
        fields=[
            'name',
            'comment',
        ]


