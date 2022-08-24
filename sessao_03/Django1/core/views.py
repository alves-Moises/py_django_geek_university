from django.shortcuts import render

def index(request):
    context = {
        "curso": "programaçãop web com django framework",
        "outro":  "Django Django"
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')