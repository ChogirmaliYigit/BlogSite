from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.serializers import CategorySerializer, FoodSerializer, OrderItemSerializer, OrderSerializer, ClientSerializer
from main.models import Category, Food, Order, OrderItem, Client


class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class FoodCreateListView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = 'pk'


class OrderCreateListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'


class OrderItemCreateListView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'pk'


class ClientCreateListView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

