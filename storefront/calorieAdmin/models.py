from django.db import models

# Create your models here.
class calorie(models.Model):
  firstName = models.CharField(max_length = 50)
  title = models.CharField(max_length = 100, default='Default Title')
  calorieInput = models.IntegerField(default=0)

  def __str__(self):
    return self.title