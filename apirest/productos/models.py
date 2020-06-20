from django.db import models

class Beer(models.Model):
  brand = models.CharField(max_length=50)
  alcohol = models.DecimalField(max_digits=4, decimal_places=2)
  milliliters = models.IntegerField()
  hadmade = models.BooleanField()
  nationality = models.CharField(max_length=50, blank=True, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  edited_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.brand