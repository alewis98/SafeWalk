from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .forms import NameForm


def index(request):
    nums = [1,2,3,4,5]
    name = 'Andrew Lewis'
    args = {'name': name, 'numbers': nums}
    return render(request, 'routefinder/login.html', args)


def get_name(request):

    if request.method == 'POST':

        form = NameForm(request.POST)
        
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')

    else: 
        form = NameForm()

    return render(request, 'name.html', {'form': form})