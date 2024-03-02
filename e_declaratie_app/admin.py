from django.contrib import admin
from django.contrib.auth.models import User, Group
from authentication_app.models import Company
from .models import ExtraUserInformations

'''Unregister the Group model from the admin interface, as we won't be using it.'''
admin.site.unregister(Group)

'''Register Company model in admin interface'''
admin.site.register(Company)

'''Register ExtraUserInformations in admin interface'''
admin.site.register(ExtraUserInformations)

