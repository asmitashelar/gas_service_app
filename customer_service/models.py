from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer name
    email = models.EmailField(unique=True)  # Customer email
    phone = models.CharField(
        max_length=15, blank=True, null=True
    )  # Optional phone number
    address = models.TextField(blank=True, null=True)  # Optional address

    def __str__(self):
        return self.name  # Display customer name in dropdowns


class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ("GAS_LEAK", "Gas Leak"),
        ("INSTALLATION", "New Installation"),
        ("MAINTENANCE", "Maintenance"),
    ]
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Link to Customer

    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    attached_file = models.FileField(upload_to="attachments/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"{self.service_type} - {self.customer.name}"


class RequestStatus(models.Model):
    request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Pending")
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Status for {self.request}"
