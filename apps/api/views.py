from django.shortcuts import render

# Create your views here.
def index(request):
    # Bu funksiya 'templates' papkasidagi 'home.html' faylini topadi
    # va uni brauzerga yuboradi.
    return render(request, 'base.html')
def report_view(request):
    return render(request, "report.html")