from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
    context = {'name': 'John Doe'}
    # Renders the 'my_template.html' template
    return render(request, 'Home/Home.html', context)

def colcom_ai(request):
    return render(request, 'Home/colcomAI.html')
