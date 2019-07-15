from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def http(request):
    print(request)
    person_list = Person.objects.order_by('-name')
    return HttpResponse([i.name for i in person_list])
    # return render(request,'dj/index.html')
