from django.contrib import admin
from django.contrib.auth.models import Group


'''Unregister the Group model from the admin interface, as we won't be using it.'''
admin.site.unregister(Group)


