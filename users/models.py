from django.db import models
from django.contrib.auth.models import User

class ExtraUserInformations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

