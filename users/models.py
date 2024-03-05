from django.db import models
from django.contrib.auth.models import User
from user_company_app.models import Company

class ExtraUserInformations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_company = models.ManyToManyField(Company, related_name="userCompany", blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

