# Generated by Django 3.1.1 on 2020-09-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fire_date',
            field=models.DateField(default=None, verbose_name='Дата увольнения'),
        ),
        migrations.AlterField(
            model_name='post',
            name='hire_date',
            field=models.DateField(verbose_name='Дата приёма'),
        ),
    ]