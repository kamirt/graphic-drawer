from django import forms

class UploadFileForm(forms.Form):
    file  = forms.FileField(label=(''), widget=forms.FileInput(attrs = {"class":"btn btn-link"}))