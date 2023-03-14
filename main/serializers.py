from .models import Category, Food, Order, OrderItem, Client
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)

class FoodSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ('id', 'cat', 'title', 'desc', 'image', 'price', 'rating', 'category')
        read_only_fields = ('id',)

    def get_cat(self, obj):
        return obj.category.title


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id',)

class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'client', 'total_price', 'is_paid', 'shipping', 'created', 'updated', 'client_name')
        read_only_fields = ('id',)

    def get_client_name(self, obj):
        return obj.client.full_name

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    food = FoodSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('id',)
