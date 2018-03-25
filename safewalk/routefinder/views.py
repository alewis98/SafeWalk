from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .forms import NameForm


def login(request):
    nums = [1,2,3,4,5]
    name = 'Andrew Lewis'
    args = {'name': name, 'numbers': nums}
    return render(request, 'routefinder/login.html')


def get_name(request):

    if request.method == 'POST':

        form = NameForm(request.POST)
        
        if form.is_valid():

            person = form.cleaned_data
            lat = float(person["your_name"].strip().split(" ")[0])
            long = float(person["your_name"].strip().split(" ")[1])
            args = {'lat': lat, 'long': long}

            return render(request, 'routefinder/main.html', args)

    else: 
        form = NameForm()

    return render(request, 'name.html', {'form': form})