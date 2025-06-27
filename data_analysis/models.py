from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Researcher(AbstractUser):
    """
    Model użytkownika systemu rozszerzający standardowego użytkownika Django.
    Dziedziczy wszystkie standardowe pola: username, first_name, last_name, email, password, itp.
    """
    # Można dodać tutaj dodatkowe pola specyficzne dla Researcher
    bio = models.TextField(verbose_name="Biografia", blank=True)
    institution = models.CharField(verbose_name="Instytucja", max_length=255, blank=True)

    class Meta:
        verbose_name = "Badacz"
        verbose_name_plural = "Badacze"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('researcher_detail', kwargs={'pk': self.pk})


class Dataset(models.Model):
    """
    Model Dataset będzie przechowywał informacje o zbiorach danych.
    Będzie miał relację z modelem Researcher,
    ponieważ każdy zbiór danych ma właściciela (badacza, który go utworzył).
    """
    name = models.CharField(verbose_name="Nazwa", max_length=255)
    description = models.TextField(verbose_name = "Opis", blank=True)
    researcher = models.ForeignKey(Researcher,
                                   on_delete=models.CASCADE,
                                   verbose_name="Badacze")
    created_at = models.DateTimeField(verbose_name="Data utworzenia",
                                      auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(verbose_name="Data ostatniej modyfikacji",
                                      auto_now=True)

    def __str__(self):
        return self.name


class Analysis(models.Model):
    """
    Model Analysis będzie przechowywał informacje o analizach 
    przeprowadzonych na zbiorach danych. 
    Będzie miał relacje z modelem Dataset oraz Researcher.
    """
    name = models.CharField(verbose_name="Nazwa", max_length=255)
    description = models.TextField(verbose_name="Opis", blank=True)
    dataset = models.ForeignKey(Dataset,
                                on_delete=models.CASCADE,
                                verbose_name="Zbiór danych",
                                related_name='analyses')
    researcher = models.ForeignKey(Researcher,
                                   on_delete=models.CASCADE,
                                   verbose_name="Badacze")
    created_at = models.DateTimeField(verbose_name="Data utworzenia",
                                      auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(verbose_name="Data ostatniej modyfikacji",
                                      auto_now=True)

    def __str__(self):
        return self.name


class Visualization(models.Model):
    """
    Model Visualization będzie przechowywał informacje o wizualizacjach danych.
    Będzie miał relacje z modelem Dataset oraz Researcher.
    """
    name = models.CharField(verbose_name="Nazwa", max_length=255)
    description = models.TextField(verbose_name="Opis", blank=True)
    visualization_type = models.CharField(verbose_name="Typ wizualizacji",
                                          max_length=255,
                                          blank=True)
    dataset = models.ForeignKey(Dataset,
                                on_delete=models.CASCADE,
                                verbose_name="Zbiór danych")
    created_at = models.DateTimeField(verbose_name="Data utworzenia",
                                      auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(verbose_name="Data ostatniej modyfikacji",
                                      auto_now=True)
    researcher = models.ForeignKey(Researcher,
                                   on_delete=models.CASCADE,
                                   verbose_name="Badacze")

    def __str__(self):
        return self.name
