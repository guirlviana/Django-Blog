from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=255, verbose_name='Autor')
    email_comentario = models.EmailField(max_length=255, verbose_name='Email')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário', blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Está público?')

    def __str__(self) -> str:
        return self.nome_comentario
