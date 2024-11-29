from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, ServiceRequest, RequestStatus
from .forms import ServiceRequestForm


def home(request):
    return redirect("submit_request")  # Redirects to the service request form


def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save()
            # Automatically create a status for the new request
            RequestStatus.objects.create(request=service_request, status="Pending")
            return redirect("track_request", request_id=service_request.id)
    else:
        form = ServiceRequestForm()

    return render(request, "customer_service/submit_request.html", {"form": form})


def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    request_status = RequestStatus.objects.get(request=service_request)

    return render(
        request,
        "customer_service/track_request.html",
        {
            "service_request": service_request,
            "request_status": request_status,
        },
    )
