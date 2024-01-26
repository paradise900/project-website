from django.shortcuts import render


def index(request):
    data = {
        'title': "Немного информации",

    }
    return render(request, 'main/web.html', data)

