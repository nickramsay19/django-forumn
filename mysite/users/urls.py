from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('<int:user_id>', views.profile, name='profile'),
]