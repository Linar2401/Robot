from django.shortcuts import render


# Create your views here.
def controller(request):
    return render(request, 'main.html')

