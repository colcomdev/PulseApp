from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)
    approvers = models.ManyToManyField(User, related_name="department_approvers")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=20, choices=[
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
        ('IT', 'IT'),
        ('SECURITY', 'Security'),
    ])

    def __str__(self):
        return self.user.username


class System(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AccessRequest(models.Model):
    LEVELS = [
        ('MANAGER', 'Manager Approval'),
        ('IT', 'IT Approval'),
        ('SECURITY', 'Security Approval'),
        ('DONE', 'Completed'),
    ]

    STATUS = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    reason = models.TextField()

    current_level = models.CharField(max_length=20, choices=LEVELS, default='MANAGER')
    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)

#==================================================================================================================
# models.py
from django.db import models

class SecurityLog(models.Model):
    OWNERSHIP_CHOICES = [
        ('Company Items', 'Company Items'),
        ('Personal/Other', 'Personal / Other'),
    ]

    name = models.CharField(max_length=255)
    badge = models.CharField(max_length=100)
    ownership = models.CharField(max_length=50, choices=OWNERSHIP_CHOICES)

    department = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)

    items = models.TextField()
    vehicle = models.CharField(max_length=50, blank=True, null=True)

    comments = models.TextField(blank=True, null=True)
    entry_time = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.entry_time}"


class ApprovalLog(models.Model):
    request = models.ForeignKey(AccessRequest, on_delete=models.CASCADE)
    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)  # APPROVED / REJECTED
    level = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)