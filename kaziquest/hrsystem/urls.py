from django.urls import include, path, re_path
from rest_framework import routers
from .views import EmployeeViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'hr', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_employee/', EmployeeViewSet.as_view({'post': 'create'}), name='hr-detail'),
    path('d/', EmployeeViewSet.as_view({'post': 'dummy'}), name='hr-detail'),
    path('verify_email/<str:token>/', EmployeeViewSet.as_view({'get': 'verify_email'}), name='verify_email'),
    # add a new route to retrieve a specific employee by ID
    path('hr/<str:pk>/', EmployeeViewSet.as_view({'get': 'retrieve'}), name='hr-detail'),
    # add a new route to update an employee by ID
    path('hr/<str:pk>/update/', EmployeeViewSet.as_view({'put': 'update'}), name='hr-update'),
    # add a new route to delete an employee by ID
    path('hr/<str:pk>/delete/', EmployeeViewSet.as_view({'delete': 'destroy'}), name='hr-delete'),

]

# add the following lines to allow CORS for all API endpoints
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
@csrf_exempt
def csrf(request):
    return Response({'detail': 'CSRF cookie set'})

urlpatterns += [
    re_path(r'^api-auth/csrf/$', csrf),
]
