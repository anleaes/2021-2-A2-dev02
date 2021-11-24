from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('editar/<int:id_user>/', views.edit_profile, name='edit_profile'),
]