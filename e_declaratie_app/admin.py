from django.contrib import admin
from django.contrib.auth.models import Group
from companies.models import Company

'''Unregister the Group model from the admin interface, as we won't be using it.'''
admin.site.unregister(Group)

'''Register Company model in admin interface'''
admin.site.register(Company)



