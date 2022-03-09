from django.shortcuts import render
from . import forms
# Create your views here.
def regform(request):
    form = forms.AnimalForm()
    if request.method == 'POST':
        form = forms.AnimalForm(request.POST)
        message = 'Thank you!'
    else:
        message = 'Input your animal infomation!'
    return render(request, 'animalinfo.html', {'message': message, 'form': form})
