
from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Person
from django.template import loader
# Create your views here.
def index(request):
    latest_Person_list = Person.objects.order_by('-id')[:5]
    template = loader.get_template('asigm_1_app/index.html')
    context = {
        'latest_Person_list': latest_Person_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'asigm_1_app/detail.html', {'person': person})
