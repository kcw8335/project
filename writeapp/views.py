from django.shortcuts import render

def writeapp(request):
    return render(request, 'writeapp.html')