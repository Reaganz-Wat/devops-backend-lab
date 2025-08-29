from django.shortcuts import render
from rest_framework import viewsets
from .models import Products, User, Orders
from .serializers import ProductSerializer, UserSerializer, OrderSerializer
from .tasks import send_welcome_email

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        # Save the user first
        user = serializer.save()

        # 🚀 Trigger Celery task after successful save
        send_welcome_email.delay(user.username)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        send_welcome_email.delay("This is a test product")
        return super().perform_create(serializer)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer