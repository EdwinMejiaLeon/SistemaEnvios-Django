from django.shortcuts import render
#vamos a importar los servicios  puestos en la administracion 
from blog.models import Post

# Create your views here.
def blog (request):
    #con esto importa los servicios contruidos
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts":posts})