from django.db import models
from movies.models import Movies
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Avaliação não pode ser inferior a 0 estrelas."),
            MaxValueValidator(5, "Avaliação não pode ser superior a 5"),
        ]
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.movie
