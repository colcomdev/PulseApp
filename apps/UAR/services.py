from django.core.mail import send_mail
from django.conf import settings
from .models import ApprovalLog


def send_notification(user, subject, message):
    if user.email:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


def process_approval(request_obj, user, action):
    # Log action
    ApprovalLog.objects.create(
        request=request_obj,
        approver=user,
        action=action,
        level=request_obj.current_level
    )

    if action == "REJECTED":
        request_obj.status = "REJECTED"
        request_obj.save()
        return

    # Move workflow forward
    if request_obj.current_level == "MANAGER":
        request_obj.current_level = "IT"

    elif request_obj.current_level == "IT":
        request_obj.current_level = "SECURITY"

    elif request_obj.current_level == "SECURITY":
        request_obj.current_level = "DONE"
        request_obj.status = "APPROVED"

    request_obj.save()