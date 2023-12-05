from django.db import models


class Item(models.Model):
    name = models.CharField(
        'Наименование',
    )
    description = models.TextField(
        'Описание',
    )
    price = models.PositiveIntegerField(
        'Цена',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
