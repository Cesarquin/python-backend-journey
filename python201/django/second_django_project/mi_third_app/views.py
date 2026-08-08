from django.shortcuts import render

# Create your views here.
def mivista(request):
    return render(request, 'mi_third_app\pagina.html')
