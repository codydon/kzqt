from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
     # employee
    path('create_employee/', views.create_employee, name='create_employee'),
    # leavedays
    path('create_leave/', views.create_leave, name='create_leave'),
    # assets
    path('assets_save/', views.create_asset, name='assets_save'),
    # asset_track
    path('create_track/', views.create_asset_track, name='create_track'),

# dummy
    path('d/', views.d, name='d'),
]

