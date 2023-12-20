from django.urls import re_path

from . import views
from .views import ProductListView, CartItemListView

urlpatterns = [
    re_path('signup/', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    
]
