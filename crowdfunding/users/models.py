from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
  date_of_birth = models.DateField(null=True, blank=True)
  gender = models.CharField(max_length=10, null=True, blank=True)
  street_address = models.CharField(max_length=255, null=True, blank=True)
  suburb = models.CharField(max_length=100, null=True, blank=True)
  state = models.CharField(max_length=100, null=True, blank=True)
  postcode = models.CharField(max_length=20, null=True, blank=True)
  phone_number = models.CharField(max_length=20, null=True, blank=True)
  profile_image = models.URLField(null=True, blank=True) 
  def __str__(self):
   return self.username
