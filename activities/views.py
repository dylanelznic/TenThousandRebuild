from django.http import HttpResponse
from django.shortcuts import render, redirect
from activities.models import Activity

# Create your views here.
def home_page(request):
	return render(request, 'home.html')

def new_activity(request):
	new_activity = Activity.objects.create(text=request.POST['activity_text'])
	return redirect(f'/activities/{new_activity.id}/')

def view_activity(request, activity_id):
	activity = Activity.objects.get(id=activity_id)
	return render(request, 'activity.html', {'activity': activity})