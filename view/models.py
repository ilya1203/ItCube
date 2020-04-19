from django.db import models

class People(models.Model):
    Name = models.CharField(max_length=50)
    YearsOne = models.CharField(max_length=20)
    YearsTwo = models.CharField(max_length=20)
    Place = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['Name']
