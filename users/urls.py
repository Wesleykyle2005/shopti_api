from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    UserCreateView, 
    TokenObtainPairView,
    MunicipalityDetailView, 
    DepartmentDetailView, 
    DepartmentListView,
    LocationViewSet
    )

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='user-login'),
    path('municipality/<int:pk>/', MunicipalityDetailView.as_view(), name='municipality-detail'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
]
