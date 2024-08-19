from django.urls import include, path
from . import user_lists_views

urlpatterns = [
    path('', user_lists_views.user_lists, name='user_lists'),
]