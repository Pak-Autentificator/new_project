from django.urls import path
from . import views
from .views import Search

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('order/checkout/', views.order_checkout, name='order_checkout'),
    path('search', Search.as_view, name='search'),
]