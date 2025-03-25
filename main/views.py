from django.shortcuts import render, redirect

from .models import Repair, Shipment
from django.contrib import messages
from django.http import HttpResponse, Http404
from .forms import ShipmentCreateForm, RepairCreateForm

def index_view(request):
    return render(request, 'main/index.html')

from django.shortcuts import render, redirect
from .forms import ShipmentCreateForm, RepairCreateForm
from django.contrib import messages

def create_shipment_view(request):
    if not request.user.is_authenticated:
        raise Http404()

    if request.method == 'POST':
        # Check which form to process based on 'shipment_type'
        shipment_type = request.POST.get('shipment_type')

        # Initialize the correct form
        shipment_form = ShipmentCreateForm(request.POST, request.FILES)
        repair_form = RepairCreateForm(request.POST, request.FILES)

        if shipment_form.is_valid():
            shipment_object = shipment_form.save(commit=False)
            shipment_object.user = request.user  # Assign the user to the shipment
            shipment_object.save()

            # If it's a repair shipment, create repair object
            if shipment_type == 'repair' and repair_form.is_valid():
                repair_object = repair_form.save(commit=False)
                repair_object.shipment = shipment_object  # Link repair to shipment
                repair_object.save()

                messages.success(request, "Repair shipment created successfully.")
                return redirect('index')  # Redirect to the index after creating a repair shipment
            else:
                messages.success(request, "Regular shipment created successfully.")
                return redirect('index')  # Redirect to the index after creating a regular shipment

    else:
        shipment_form = ShipmentCreateForm()
        repair_form = RepairCreateForm()

    return render(request, 'main/create_shipment.html', {
        'shipment_form': shipment_form,
        'repair_form': repair_form
    })


def user_profile_view(request):
    if not request.user.is_authenticated:
        raise Http404()

    return render(request, 'main/user_profile.html')

def shipments_view(request):
    if not request.user.is_authenticated:
        raise Http404

    shipments = Shipment.objects.filter(user=request.user)
    return render(request, 'main/shipments_view.html', {'shipments': shipments})

# def repair_create_view(request):
#     if request.method == 'GET':
#         form = RepairCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, "Repair created successfully.")
#             return redirect('user_profile')
#         else:
#             form = RepairCreateForm()
#         return render(request, 'main/repair_create.html', {'form': form})

