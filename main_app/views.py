from django.shortcuts import render, redirect

# Create your views here.
def root(request):
    return redirect("/index")

def index(request):
    if "number" in request.session:
        request.session['number'] += 1
    else:
        request.session['number'] = 1
    return render(request,"index.html")

def reset(request):
    request.session.clear()
    return redirect("/")