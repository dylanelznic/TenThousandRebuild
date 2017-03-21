from django.http import HttpResponse
from django.shortcuts import render, redirect
from activities.models import Activity

# Create your views here.
def home_page(request):
	return render(request, 'home.html')

def new_activity(request):
	Activity.objects.create(text=request.POST['activity_text'])
	return redirect('/activities/the-only-activity-in-the-world/')

def view_activity(request):
	activity = Activity.objects.last()
	return render(request, 'activity.html', {'activity': activity})