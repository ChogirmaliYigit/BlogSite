from django.urls import path
from .views import CategoryCreateListView, CategoryRetrieveUpdateDestroyAPIView, FoodCreateListView, FoodRetrieveUpdateDestroyAPIView, OrderCreateListView, OrderRetrieveUpdateDestroyAPIView, OrderItemCreateListView, OrderItemRetrieveUpdateDestroyAPIView, ClientCreateListView, ClientRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('cats/', CategoryCreateListView.as_view(), name='cats'),
    path('cat/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='cat_detail'),
    path('foods/', FoodCreateListView.as_view(), name='foods'),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyAPIView.as_view(), name='food_detail'),
    path('orders/', OrderCreateListView.as_view(), name='orders'),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order_detail'),
    path('order-items/', OrderItemCreateListView.as_view(), name='order_items'),
    path('order-item/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='order_item_detail'),
    path('clients/', ClientCreateListView.as_view(), name='clients'),
    path('client/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_detail'),
]
