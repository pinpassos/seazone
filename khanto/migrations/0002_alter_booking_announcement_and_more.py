# Generated by Django 4.2.2 on 2023-07-01 04:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('khanto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='announcement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khanto.announcement'),
        ),
        migrations.AlterField(
            model_name='property',
            name='number_of_guests',
            field=models.PositiveIntegerField(help_text='Max number of guests', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Number of guests'),
        ),
    ]
