from django.db import models

class People(models.Model):
    Name = models.CharField(max_length=50, verbose_name='ФИО')
    YearsOne = models.CharField(max_length=20,verbose_name='Дата рождения')
    YearsTwo = models.CharField(max_length=20,verbose_name='Дата смерти')
    Place = models.TextField(blank=True,verbose_name='Место призыва')
    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['Name']
