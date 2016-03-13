from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libsys.models import Student
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy




#from django.http import HttpResponse

def index(request):
	return render(request, 'libsys/index.html')

def contact(request):
	return render(request, 'libsys/contact.html')

def service(request):
	return render(request, 'libsys/service.html')

def about(request):
	return render(request, 'libsys/about.html')



#class StuList(ListView):
	#model=Student

#class  StuDetail(DetailView):
	#model=Student

#class  StuCreate(CreateView):
	#model=Student
	#fields=['name', 'regno', 'accno', 'address']

#class  StuUpdate(UpdateView):
	#model=Student
	#fields=['name', 'regno', 'accno', 'address']

#class  StuDelete(DeleteView):
	#model=Student
	#success_url= reverse_lazy('stu_list')




@login_required
def submit_session(request):
 	return render(request, 'libsys/submit_session.html')





