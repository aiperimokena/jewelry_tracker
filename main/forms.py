from django import forms
from .models import Shipment, Repair


class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = (
            'title',
            'tracking_number',
            'carrier',
            'status',
            'commercial_invoice',
            'shipping_to',
            'shipping_from',
            'shipped_date',
            'notes'
        )

        widgets = {
            'shipped_date': forms.SelectDateWidget(years=range(2020, 2030)),
            'delivery_date': forms.SelectDateWidget(years=range(2020, 2030)),
        }

class RepairCreateForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = (
            'title',
            'status',
            'repair_start_date',
            'repair_end_date',
            'received_date',
            'shipped_date',
            'proof_of_delivery',
            'notes'
        )
