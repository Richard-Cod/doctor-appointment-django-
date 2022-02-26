# Generated by Django 4.0.1 on 2022-02-25 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctors', '0008_alter_openhour_doctor_doctorreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctor', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
