from django.shortcuts import render

# Create your views here.

def home(request):
    m="Hola Biblioteca"
    context = {"mensaje":m}
    return render(request,'home.html',context)
