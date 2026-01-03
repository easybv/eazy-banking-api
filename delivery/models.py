from django.db import models
from django.utils import timezone

# Create your models here.


class DeliveryDetails(models.Model):
    tracking_code = models.CharField(max_length=200, blank=True, null=True)
    shipper_name = models.CharField(max_length=200, blank=True, null=True)
    shipper_location = models.CharField(max_length=200, blank=True, null=True)
    shipper_phone_number = models.CharField(
        max_length=200, blank=True, null=True)
    receiver_name = models.CharField(max_length=200, blank=True, null=True)
    receiver_location = models.CharField(max_length=200, blank=True, null=True)
    receiver_phone_number = models.CharField(
        max_length=200, blank=True, null=True)
    # shipping information
    destination = models.CharField(max_length=200, blank=True, null=True)
    weight = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    total_freight = models.CharField(max_length=200, blank=True, null=True)
    pickup_date = models.DateField(default=timezone.now)
    comments = models.CharField(max_length=200, blank=True, null=True)
    package = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True)
    shipment_mode = models.CharField(max_length=200, blank=True, null=True)
    qty = models.CharField(max_length=200, blank=True, null=True)
    expected_delivery_date = models.DateField(default=timezone.now)
    pickup_time = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=200, blank=True, null=True)
    type_of_shipment = models.CharField(max_length=200, blank=True, null=True)
    payment_method = models.CharField(max_length=200, blank=True, null=True)
    departure_time = models.TimeField(default=timezone.now)
    piece_type = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
