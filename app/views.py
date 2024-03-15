from django.shortcuts import render

# Create your views here.
def carousel_cdn(request):
    return render(request,'carousel_cdn.html')


def carousel_cdn_1(request):
    return render(request,'carousel_cdn_1.html')

def alerts(request):
    return render(request,'alerts.html')

def badge(request):
    return render(request,'badge.html')