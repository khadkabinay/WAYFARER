from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    # return render(request, 'home.html')
    return render(request, 'profile/index.html')
