from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from posts.models import Like

from posts.models import Post

posts = Post.objects.order_by('-id')

def index(request):
    return render(request, 'index.html')

def listar_posts(request):
    return render(request, 'index.html', {'posts': posts})

def postar(request):
    if request.method == 'POST':
        post = Post()
        post.autor = request.POST.get('autor')
        post.mensagem = request.POST.get('mensagem')
        post.qtd_curtidas = 0
        post.save()
        return JsonResponse({'new-post': post})

def curtir(request, id):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        likedpost = Post.objects.filter(id = id) 
        post_curtido = Like(post=likedpost) 
        post_curtido.save()  
        return JsonResponse({'like': post_curtido})
   