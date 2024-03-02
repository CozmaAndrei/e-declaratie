from django.db import models
from django.contrib.auth.models import User

'''Adding more fields in User model using another model/table'''
class ExtraUserInfo(models.Model):
    extra_user = models.OneToOneField(User, related_name='extrainfo', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    
    class Meta:
        verbose_name = 'Extra User Informations'
        verbose_name_plural = 'Extra User Informations'
        
    def __str__(self):
        return str(self.extra_user)