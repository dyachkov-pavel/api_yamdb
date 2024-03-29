# Generated by Django 3.0.5 on 2020-12-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0002_auto_20201217_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, verbose_name='Оценка от 1 до 10'),
            preserve_default=False,
        ),
    ]
