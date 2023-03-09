from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
   
    # dummy
    path('dd/', views.d, name='d'),
]

