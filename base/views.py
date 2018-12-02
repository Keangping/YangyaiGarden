from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, 'base/index.html')

def about(request):
	return render(request, 'base/about.html')

def contactus(request):
	return render(request, 'base/contactus.html')

def service(request):
	return render(request, 'base/service.html')

def event(request):
	return render(request, 'base/event.html')

def property(request):
	return render(request, 'base/property.html')

def activity(request):
	return render(request, 'base/activity.html')