from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        ordering = ['name']
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.name
