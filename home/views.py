<<<<<<< HEAD
# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'sobre.html')
def contato(request):
    return render(request, 'contato.html') 
def ajuda (request): 
=======
# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'sobre.html')
def contato(request):
    return render(request, 'contato.html') 
def ajuda (request): 
>>>>>>> e84f4e8dfe6c3fa3fcee23e7a5092c49c0a68f24
    return render(request, 'ajuda.html')