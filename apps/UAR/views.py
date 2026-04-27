from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AccessRequest, UserProfile, SecurityLog
from .forms import RequestForm
from .services import process_approval
from .forms import SecurityLogForm
from django.http import HttpResponse

# views.py


def is_approver(user):
    return user.groups.filter(name="Approvers").exists()


@login_required
def dashboard(request):
    user = request.user

    if is_approver(user):
        profile = user.userprofile
        requests = AccessRequest.objects.filter(
            department=profile.department,
            status="PENDING"
        )
    else:
        requests = AccessRequest.objects.filter(user=user)

    return render(request, "dashboard/dashboard.html", {"requests": requests})


@login_required
def create_request(request):
    form = RequestForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.department = request.user.userprofile.department
        obj.save()
        return redirect("dashboard")

    return render(request, "uar/create_request.html", {"form": form})


@login_required
def approve(request, id):
    req = get_object_or_404(AccessRequest, id=id)

    if not is_approver(request.user):
        return redirect("dashboard")

    process_approval(req, request.user, "APPROVED")

    return redirect("dashboard")


@login_required
def reject(request, id):
    req = get_object_or_404(AccessRequest, id=id)

    if not is_approver(request.user):
        return redirect("dashboard")

    process_approval(req, request.user, "REJECTED")

    return redirect("dashboard")



#==============================SECURITY ACCESS LOG===================================================================
# views.py

def security_entry(request):
    if request.method == 'POST':
        form = SecurityLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs')  # create a success page
    else:
        form = SecurityLogForm()

    return render(request, 'uar/SAL.html', {'form': form})


def success(request):
    return render(request, 'uar/success.html')






def security_logs(request):
    ownership = request.GET.get('ownership', 'All')
    export = request.GET.get('export')

    logs = SecurityLog.objects.all()

    if ownership != 'All':
        logs = logs.filter(ownership=ownership)

    logs = logs.order_by('-entry_time')

    # ✅ EXPORT BLOCK
    if export == '1':
        import pandas as pd  # keep import here

        data = logs.values(
            'name', 'badge', 'ownership', 'department',
            'purpose', 'items', 'vehicle', 'comments', 'entry_time'
        )

        df = pd.DataFrame(list(data))

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=security_logs.xlsx'
        # Convert all timezone-aware datetime columns to timezone-naive
        for col in df.select_dtypes(['datetime', 'datetimetz']).columns:
            df[col] = df[col].dt.tz_localize(None)

        # Now export will work
        df.to_excel(response, index=False)


        return response  # ✅ IMPORTANT

    # ✅ ALWAYS RETURN THIS FOR NORMAL PAGE
    return render(request, 'uar/logs.html', {
        'logs': logs,
        'ownership': ownership
    })
#=========================================================================================================================


"""
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # --- PHASE 1: READ FROM FILE ---
    # Replace 'data.csv' or 'data.xlsx' with your actual file path
    return HttpResponse("Hello Manlow we are in Django now in Apps")


def RequestRights(request):
    
    return render(request,"UAR/requests.html")


def ApproveRights(request):
    
    return render(request,"UAR/approver_dashboard.html")

def RequestDetails(request):
    
    return render(request,"UAR/approver_details.html")"""


