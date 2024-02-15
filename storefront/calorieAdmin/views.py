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
  calorieDB.save()
  names = calorie.objects.all()
  # return render(request, 'home.html', {'name': calorie.objects.all()[0].firstName})
  # return render(request, 'home.html', {'name': username})
  return render(request, 'home.html', {'names': names, 'username': username})
