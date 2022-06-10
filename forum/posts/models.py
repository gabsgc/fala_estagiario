from django.db import models

class Post(models.Model):
    autor = models.TextField()
    mensagem = models.CharField(max_length=200)
    qtd_curtidas = models.IntegerField()
    data_postagem = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)