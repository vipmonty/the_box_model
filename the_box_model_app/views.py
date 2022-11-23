from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'the_box_model_app/index.html')
