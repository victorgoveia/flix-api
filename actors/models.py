from django.db import models
from django_countries.fields import CountryField


class Actor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    death_date = models.DateField(null=True, blank=True, verbose_name="Data de Falecimento")
    nationality = CountryField(verbose_name="Nacionalidade")
    biography = models.TextField(blank=True, verbose_name="Biografia")
    # photo = models.ImageField(upload_to='actors/', null=True, blank=True, verbose_name="Foto")
    height = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name="Altura (m)")
    social_media = models.JSONField(null=True, blank=True, verbose_name="Redes Sociais")
    active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        ordering = ['name']
        verbose_name = "Ator"
        verbose_name_plural = "Atores"

    def __str__(self):
        return self.name
