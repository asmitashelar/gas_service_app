from django.contrib import admin
from .models import ServiceRequest, Customer


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "service_type",
        "status",
        "submitted_at",
        "updated_at",
    )  # Display these fields in the admin panel
    list_filter = ("status", "service_type")  # Add filters for easier management
    search_fields = (
        "customer__name",
        "service_type",
    )  # Enable search by customer name or request type
    ordering = ("-submitted_at", "-updated_at")  # Order by the latest requests
    list_editable = ("status",)  # Allow inline editing of the status


admin.site.register(Customer)
