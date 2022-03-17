from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)