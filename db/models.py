from django.db import models
from django.urls import reverse


class OilField(models.Model):
    name = models.CharField(max_length=100, verbose_name='Месторождение')
    type = models.CharField(max_length=100, verbose_name='Тип')
    location = models.CharField(max_length=100, verbose_name='Расположение')
    owner = models.CharField(max_length=100, verbose_name='Недропользователь')
    description = models.TextField(blank=True, verbose_name='Описание')
    obzor_img = models.ImageField(blank=True, upload_to='maps', height_field=None, width_field=None, max_length=100,
                                  verbose_name='Обзорная карта')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):  # new
    #     return reverse('field_detail', args=[str(self.id)])


class Well(models.Model):
    name = models.CharField(max_length=100, unique=True)
    field = models.ForeignKey(
        OilField, related_name='wells', on_delete=models.CASCADE)

    type = models.CharField(max_length=100, blank=True, null=True)
    altitude = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    x = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    y = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    md = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'field',)

    def __str__(self):
        return self.name