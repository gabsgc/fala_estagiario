from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Like

from posts.models import Post

posts = Post.objects.order_by('-id')

def index(request):
    return render(request, 'index.html', {'posts': posts})

def postar(request):
    if request.method == 'POST':
        post = Post()
        post.autor = request.POST.get('autor')
        post.mensagem = request.POST.get('mensagem')
        post.qtd_curtidas = 0
        post.save()
        return render(request, 'index.html', {'posts': posts})
    return render(request, 'index.html', {'posts': posts})

def curtir(request):
    if request.method == 'GET':
        post_id = request.GET['id']
        likedpost = Post.objects.filter(id = post_id) 
        post_curtido = Like(post=likedpost) 
        post_curtido.save()  
        return HttpResponse("Success!") 
   