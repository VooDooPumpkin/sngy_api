from django.db import models


class Post(models.Model):
    name = models.CharField('Имя', max_length=200)
    company_name = models.CharField('Компания', max_length=100)
    position_name = models.CharField('Должность', max_length=100)
    hire_date = models.DateField('Дата приёма')
    fire_date = models.DateField('Дата увольнения', default=None, null=True)
    salary = models.IntegerField('Ставка, руб.')
    fraction = models.IntegerField('Ставка, %')
    base = models.IntegerField('База, руб.')
    advance = models.IntegerField('Аванс, руб.')
    by_hours = models.BooleanField('Почасовая оплата')

    def __str__(self):
        return f'{self.name} - {self.position_name} ({self.company_name})'
