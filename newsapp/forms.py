from django import forms
from .models import User_model,Login

class DateInput(forms.DateInput):
    input_type = 'date'

class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)

class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'my_date_field' : DateInput()}


class hereglegch_burtgeh(forms.ModelForm):
    class Meta:
        model = User_model
        fields = ['lastname', 'firstname', 'email', 'name', 'password']

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()