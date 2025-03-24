
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Repair(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('in_progress', 'In progress'),
        ('shipped', 'Shipped')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(
        max_length=123,
        verbose_name='Title'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='received')

    repair_start_date = models.DateTimeField()
    repair_end_date = models.DateTimeField(
        null=True,
        blank=True)
    received_date = models.DateTimeField()
    shipped_date = models.DateTimeField(
        null=True,
        blank=True)
    proof_of_delivery = models.ImageField(
        upload_to='proofs',
        blank=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Repair shipment'
        verbose_name_plural = 'Repair shipments'

    def __str__(self):
        return f'{self.title} --> {self.status}'


class Shipment(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('in_progress', 'In progress'),
        ('shipped', 'Shipped'),
        ('received', 'Received')
    ]
    CARRIER_CHOICES = [
        ('fedex', 'FedEx'),
        ('dhl', 'DHL'),
        ('ferrari', 'FERARRI'),
        ('other', 'OTHER')

    ]
    STORE_CHOICES = [
        ('harrods', 'Harrods'),
        ('liberty', 'Liberty'),
        ('dublin', 'Dublin'),
        ('dubai_mall', 'Dubai Mall'),
        ('moe', 'MOE')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(
        max_length=123,
        verbose_name='Title'
    )
    tracking_number = models.CharField(
        max_length=100,
        unique=True)
    carrier = models.CharField(
        max_length=10,
        choices=CARRIER_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES)
    commercial_invoice = models.ImageField(
        upload_to='proofs/',
        blank=True, null=True)
    shipping_to = models.CharField(
        max_length=100,
        choices=STORE_CHOICES)

    shipping_from = models.CharField(
        max_length=100,
        choices=STORE_CHOICES)
    shipped_date = models.DateField(
            null=True,
            blank=True
        )
    delivery_date = models.DateTimeField(
        null=True,
        blank=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    notes = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Shipment {self.title} --> {self.status}"

