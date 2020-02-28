from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    # View code here...
    context = {'data': 'None'}
    return render(request, 'base.html', context)