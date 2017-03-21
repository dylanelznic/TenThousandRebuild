from django.http import HttpResponse
from django.shortcuts import render, redirect
from activities.models import Activity

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Activity.objects.create(text=request.POST['activity_text'])
		return redirect('/activities/the-only-activity-in-the-world/')

	activity = Activity.objects.last()
	return render(request, 'home.html', {'activity': activity})