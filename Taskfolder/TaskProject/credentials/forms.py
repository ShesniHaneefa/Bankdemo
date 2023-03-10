from django.contrib import admin
from credentials.models import District, Acc_type, Details
from django import forms


class District_form(forms.Form):
    class Meta:
        model=District
        fields=['name']

class Acc_form(forms.Form):
    class Meta:
        model=Acc_type
        fields=['name']

class Details_form(forms.Form):
    class Meta:
        model=Details
        fields=['name','dob','age','contact','email','address','branch']
