import os
from django.db import models
from django.contrib.auth.models import User
from companies.models import Company
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    '''This function is used to create a new folder for each user and save his profile picture in it. 
        The folder name is the user's username.
        The function are used in the ExtraUserInformations model in the user_pic field.'''
    new_name_of_folder = f"{instance.user.username}'s_pics"
    filename = instance.user.username + '.png'
    return os.path.join('user_pics', new_name_of_folder + '/' + filename)

class ExtraUserInformations(models.Model):
    '''This model is used to store extra informations about the user, like his profile picture, date of birth, etc.'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_company = models.ManyToManyField(Company, related_name="user_companies", blank=True)
    favorite_user = models.ManyToManyField(User, related_name="favorite_users", blank=True, symmetrical=False)
    favorite_company = models.ManyToManyField(Company, related_name="favorite_companies", symmetrical=False, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    user_pic = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    
    def __str__(self):
        return self.user.username



       