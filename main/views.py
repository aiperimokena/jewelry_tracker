from django.shortcuts import render, redirect

from .models import Repair, Shipment
from django.contrib import messages
from django.http import HttpResponse, Http404
from .forms import ShipmentCreateForm, RepairCreateForm

def index_view(request):
    return render(request, 'main/index.html')

def create_shipment_view(request):
    if not request.user.is_authenticated:
        raise Http404()

    if request.method == 'POST':
        shipment_form = ShipmentCreateForm(request.POST, request.FILES)
        repair_form = RepairCreateForm(request.POST, request.FILES)

        if shipment_form.is_valid():
            shipment_object = shipment_form.save(commit=False)
            shipment_object.user = request.user  # Assign the user to the shipment
            shipment_object.save()

            # Check if the user selected 'repair' as shipment type
            if request.POST.get('shipment_type') == 'repair':
                messages.success(request, "Repair shipment created successfully.")
                return redirect('repair')  # Redirect to the repair page after submitting a repair shipment

            messages.success(request, "Shipment created successfully.")
            return redirect('index')  # Redirect to the index or another page after a regular shipment

    else:
        shipment_form = ShipmentCreateForm()
        repair_form = RepairCreateForm()

    return render(request, 'main/create_shipment.html', {'shipment_form': shipment_form, 'repair_form': repair_form})

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

