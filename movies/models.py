from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movies(models.Model):

    title = models.CharField(max_length=120)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name="actors")
    resume = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.title
