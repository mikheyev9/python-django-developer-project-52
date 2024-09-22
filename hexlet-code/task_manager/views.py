from django.shortcuts import render


def index(request):
    print('00')
    return render(request, 'base.html')
