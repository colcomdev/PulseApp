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
    
    return render(request,"UAR/approver_details.html")


