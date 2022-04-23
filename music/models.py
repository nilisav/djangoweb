from django.db import models


class Genre(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name="Название"
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Author(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name="Имя"
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Song(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="Жанр"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )

    def __str__(self):
        return self.name
