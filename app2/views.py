from django.shortcuts import render

# Create your views here.
def lucky(request):
    return render(request,'lucky.html')