from django.shortcuts import render

# Create your views here.

from .models import Lawyer

def lawyer_list(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'lawyers/lawyer_list.html', {'lawyers': lawyers})
