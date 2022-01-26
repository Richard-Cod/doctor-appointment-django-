# Generated by Django 4.0.1 on 2022-01-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=6),
            preserve_default=False,
        ),
    ]
