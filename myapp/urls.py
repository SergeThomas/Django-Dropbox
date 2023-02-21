from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_folder, name='open_folder'),
    path('redirect/', views.redirect_to_dropbox_folder, name='dropbox_folder'),   # not active yet.
    path('userview/', views.dropbox_user_view, name='dropbox_user_view'),
]