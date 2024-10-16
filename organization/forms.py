from django import forms

class NewQuizForm(forms.Form):
    title = forms.CharField(label="Quiz Title",max_length=255)
    description = forms.CharField(label="Description",widget=forms.Textarea)
    csvfile = forms.FileField(label="CSV File")


