from django.urls import path
from . import user_profiles_views

urlpatterns = [
    path('profile/<str:username>/', user_profiles_views.user_view_profile, name='user_view_profile'),
    path('profile/<str:username>/report/', user_profiles_views.report_user, name='report_user'),
    
]