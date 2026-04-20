from django.db import models
from django.contrib.auth.models import User


class System(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AccessRight(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserAccessRequest(models.Model):

    REQUEST_TYPES = [
        ("NEW", "New Access"),
        ("MODIFY", "Modify Access"),
        ("REMOVE", "Remove Access")
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected")
    ]

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="access_requests"
    )

    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=150)
    email = models.EmailField()

    request_type = models.CharField(
        max_length=10,
        choices=REQUEST_TYPES
    )

    system = models.ForeignKey(
        System,
        on_delete=models.CASCADE
    )

    rights_requested = models.ManyToManyField(
        AccessRight
    )

    justification = models.TextField()

    supervisor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="requests_to_approve"
    )

    supervisor_comment = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - {self.requester.username} - {self.system.name}"