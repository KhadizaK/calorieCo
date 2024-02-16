from django.shortcuts import render
from django.http import HttpResponse
from calorieAdmin.models import calorie
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def sayHello(request):
  calorieDB = calorie()
  username = request.POST.get('text1', '')
  calorieDB.firstName = username
  calorieDB.title = "test1"
  calorieInput = request.POST.get('calorieInput', 0) # get the calorie input from the request
  calorieDB.calorieInput = calorieInput # assign it to the model instance
  calorieDB.save()
  names = calorie.objects.all()
  return render(request, 'home.html', {'names': names, 'username': username, 'calorieInput': calorieInput})
