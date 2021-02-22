from django.shortcuts import render


def home_page(request):

    ''' The view to show the main homepage  '''

    return render(request, "homepage/index.html")
