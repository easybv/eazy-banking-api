from django.shortcuts import render
from django_filters import rest_framework as filters
from .models import DeliveryDetails
from rest_framework import viewsets
from .serializer import DeliverySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

class TrackingFilter(filters.FilterSet):
    tracking_code = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DeliveryDetails
        fields = ['tracking_code']


class DeliveryViewset(viewsets.ModelViewSet):
    permisson_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DeliverySerializer
    queryset = DeliveryDetails.objects.all()
    filterset_class = TrackingFilter
