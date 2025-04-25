from .models import ApproachRequest
from django import forms


class ApproachForm(forms.ModelForm):
    class Meta:
        model = ApproachRequest
        fields = ("name", "email", "message")
