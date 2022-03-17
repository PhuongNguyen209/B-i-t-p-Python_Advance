
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def sendMail(request):
    messageSent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['message']
            recipient = cd['recipient']
            if send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient]):
                messageSent = True
    else:
        form = EmailForm()
    return render(request, 'index.html', {
        'form': form,
        'messageSent': messageSent,
    })
