# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()