from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet, CategoryViewSet, OrderViewSet
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)

order_list = OrderViewSet.as_view({
    'get': 'list', 
    'post': 'create'
})

order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

category_list = CategoryViewSet.as_view({
    'get': 'list', 
    'post': 'create'
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [    
    path('', include(router.urls)),    
    re_path('register', views.register),
    re_path('test_token', views.test_token),
    re_path('login', views.login),
    path('category', category_list, name='category-list'),
    path('category/<int:pk>', category_detail, name='category-detail'),
    path('orders', order_list, name='order-list'),
    path('orders/<int:pk>', order_detail, name='order-detail'),
]
