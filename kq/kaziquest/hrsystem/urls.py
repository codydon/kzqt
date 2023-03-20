from django.urls import include, path, re_path
from rest_framework import routers
from .views import EmployeeViewSet, AssetsViewSet, NotifyViewSet, LeaveDaysViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'hr', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_employee/', EmployeeViewSet.as_view({'post': 'create_employee'}), name='hr-detail'),
    path('update_profile/', EmployeeViewSet.as_view({'post': 'update_profile'}), name='update_profile'),
    path('get_employees/', EmployeeViewSet.as_view({'get': 'get_employees'}), name='get_employees'),
    path('emplogin', EmployeeViewSet.as_view({'post': 'emplogin'}), name='emplogin'),
    path('logout/', EmployeeViewSet.as_view({'post': 'logout'}), name='logout'),
    path('reg_admin/', EmployeeViewSet.as_view({'post': 'reg_admin'}), name='reg_admin'),
    path('d/', EmployeeViewSet.as_view({'post': 'dummy'}), name='hr-detail'),
    path('getauth', EmployeeViewSet.as_view({'post': 'getauth_user'}), name='getauth'),
    path('verify_email/<str:token>', EmployeeViewSet.as_view({'post': 'verify_email'}), name='verify_email'),
    path('user_pass/', EmployeeViewSet.as_view({'post': 'user_pass'}), name='user_pass'),
    path('change_employee_role/<str:eid>/', EmployeeViewSet.as_view({'put': 'change_employee_role'}), name='change_employee_role'),
    # path('hr/<str:pk>/delete/', EmployeeViewSet.as_view({'delete': 'destroy'}), name='hr-delete'),
    # 
    path('add_asset/', AssetsViewSet.as_view({'post': 'add_asset'}), name='add_asset'),
    path('update_asset/', AssetsViewSet.as_view({'post': 'update_asset'}), name='update_asset'),
    path('assign_asset/', AssetsViewSet.as_view({'post': 'assign_asset'}), name='assign_asset'),
    path('get_assets/', AssetsViewSet.as_view({'get': 'get_assets'}), name='get_assets'),
    path('fetch_assets/<str:eid>/', AssetsViewSet.as_view({'get': 'fetch_assets'}), name='fetch_assets'),
    path('delete_asset/<str:pk>/', AssetsViewSet.as_view({'delete': 'destroy'}), name='delete_asset'),
    #
    path('leave_request', LeaveDaysViewSet.as_view({'post': 'leave_request'}), name='leave_request'),
    path('getRequests/', LeaveDaysViewSet.as_view({'get': 'getRequests'}), name='getRequests'),
    path('approveRequest/', LeaveDaysViewSet.as_view({'put': 'approveRequest'}), name='approveRequest'),
    # 
    path('notify', NotifyViewSet.as_view({'post': 'post'}) , name='notify'),
    path('get_notifications', NotifyViewSet.as_view({'get': 'get_notifications'}) , name='get_notifications'),
    path('update_read', NotifyViewSet.as_view({'put': 'update_read'}) , name='update_read'),

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
