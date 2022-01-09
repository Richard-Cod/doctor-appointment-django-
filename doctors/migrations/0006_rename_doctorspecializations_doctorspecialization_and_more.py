# Generated by Django 4.0.1 on 2022-01-08 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_alter_doctorfeature_doctor_doctorworkexperience_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DoctorSpecializations',
            new_name='DoctorSpecialization',
        ),
        migrations.CreateModel(
            name='DoctorLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='doctors.doctor')),
            ],
        ),
    ]
