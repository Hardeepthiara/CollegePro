from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libsys.models import Student
from django.views.generic import *

#from django.http import HttpResponse

def index(request):
	return render(request, 'libsys/index.html')

def contact(request):
	return render(request, 'libsys/contact.html')


# class SessionList(ListView):
# 	model=Student

# class  SessionDetail(DetailView):
# 	model=Student

@login_required
def submit_session(request):
 	return render(request, 'libsys/submit_session.html')





