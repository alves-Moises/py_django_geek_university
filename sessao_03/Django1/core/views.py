from django.shortcuts import render

def index(request):
    context = {
        "curso": "CURSO DE SEXO GRátis",
        "outro":  "Essa é a porra da variavel OUTRO< CARALHO, olha ali embaixo a variavel context sendo passada"
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')