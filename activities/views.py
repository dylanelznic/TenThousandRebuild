from django.http import HttpResponse
from django.shortcuts import render, redirect
from activities.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')

	item = Item.objects.last()
	return render(request, 'home.html', {'item': item})