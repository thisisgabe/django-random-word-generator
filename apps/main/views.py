from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def resetSession(request):
    request.session["rand_str"] = 0
    request.session["num_generated"] = 0
    print("cool")

# Create your views here.
def index(request):
    #return HttpResponse("It's Thursday my dudes")
    if(not 'num_generated' in request.session):
        resetSession(request)
    request.session['num_generated'] += 1
    request.session['rand_str'] = get_random_string(length=14)

    context = {
        'random_string' : request.session["rand_str"],
        'num_generations' : request.session["num_generated"]
    }
    return render(request, 'main/index.html', context=context)

def destroy(request):
    resetSession(request)
    return redirect('/')