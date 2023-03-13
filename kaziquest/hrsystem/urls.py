from django.urls import include, path, re_path
from rest_framework import routers
from .views import EmployeeViewSet
from .views import AssetsViewSet
from .views import NotifyViewSet

router = routers.DefaultRouter()
router.register(r'hr', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_employee/', EmployeeViewSet.as_view({'post': 'create_employee'}), name='hr-detail'),
    path('get_employees/', EmployeeViewSet.as_view({'get': 'get_employees'}), name='get_employees'),
    path('emplogin/', EmployeeViewSet.as_view({'post': 'emplogin'}), name='emplogin'),
    path('logout/', EmployeeViewSet.as_view({'post': 'logout'}), name='logout'),
    path('d/', EmployeeViewSet.as_view({'post': 'dummy'}), name='hr-detail'),
    path('getauth/', EmployeeViewSet.as_view({'get': 'getauth'}), name='getauth'),
    path('verify_email/<str:token>/', EmployeeViewSet.as_view({'get': 'verify_email'}), name='verify_email'),
    path('user_pass/', EmployeeViewSet.as_view({'post': 'user_pass'}), name='user_pass'),
    path('hr/<str:pk>/', EmployeeViewSet.as_view({'get': 'retrieve'}), name='hr-detail'),
    path('hr/<str:pk>/update/', EmployeeViewSet.as_view({'put': 'update'}), name='hr-update'),
    path('hr/<str:pk>/delete/', EmployeeViewSet.as_view({'delete': 'destroy'}), name='hr-delete'),
    # 
    path('add_asset/', AssetsViewSet.as_view({'post': 'add_asset'}), name='add_asset'),
    path('update_asset/', AssetsViewSet.as_view({'post': 'update_asset'}), name='update_asset'),
    path('assign_asset/', AssetsViewSet.as_view({'post': 'assign_asset'}), name='assign_asset'),
    path('get_assets/', AssetsViewSet.as_view({'get': 'get_assets'}), name='get_assets'),
    path('d_asset/<str:a_id>', AssetsViewSet.as_view({'post', 'delete_asset'}), name='delete_asset'),
    #
    path('notify/', NotifyViewSet.as_view()),

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
