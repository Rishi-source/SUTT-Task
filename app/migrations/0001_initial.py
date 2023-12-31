# Generated by Django 4.2 on 2023-06-08 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='register_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d')),
                ('age', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(default='Male', max_length=250)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('occupation', models.CharField(blank=True, max_length=250, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now=True, null=True)),
                ('Type_of_Doctor', models.CharField(choices=[('1', 'Cardiologist'), ('2', 'Dermatologist'), ('3', 'Endocrinologist'), ('4', 'Gastroenterologist'), ('5', 'Neurologist'), ('6', 'Oncologist'), ('7', 'Pediatrician'), ('8', 'Psychiatrist'), ('9', 'Radiologist'), ('10', 'Surgeon'), ('11', 'Orthopedic Surgeon'), ('12', 'Ophthalmologist'), ('13', 'ENT Specialist'), ('14', 'Urologist'), ('15', 'Nephrologist'), ('16', 'Pulmonologist'), ('17', 'Allergist/Immunologist'), ('18', 'Rheumatologist'), ('19', 'Hematologist'), ('20', 'Osteopath'), ('21', 'Chiropractor'), ('22', 'Homeopath'), ('23', 'Ayurvedic Doctor'), ('24', 'Naturopath'), ('25', 'Physiotherapist'), ('26', 'Dentist'), ('27', 'Veterinarian')], max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(default='Male', max_length=250)),
                ('problem', models.CharField(blank=True, max_length=550, null=True)),
                ('Day_slot', models.DateField(null=True)),
                ('time_slot', models.TimeField(null=True)),
                ('Type_of_Doctor_you_want_to_consult', models.CharField(choices=[('1', 'Cardiologist'), ('2', 'Dermatologist'), ('3', 'Endocrinologist'), ('4', 'Gastroenterologist'), ('5', 'Neurologist'), ('6', 'Oncologist'), ('7', 'Pediatrician'), ('8', 'Psychiatrist'), ('9', 'Radiologist'), ('10', 'Surgeon'), ('11', 'Orthopedic Surgeon'), ('12', 'Ophthalmologist'), ('13', 'ENT Specialist'), ('14', 'Urologist'), ('15', 'Nephrologist'), ('16', 'Pulmonologist'), ('17', 'Allergist/Immunologist'), ('18', 'Rheumatologist'), ('19', 'Hematologist'), ('20', 'Osteopath'), ('21', 'Chiropractor'), ('22', 'Homeopath'), ('23', 'Ayurvedic Doctor'), ('24', 'Naturopath'), ('25', 'Physiotherapist'), ('26', 'Dentist'), ('27', 'Veterinarian')], default='Select', max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.register_table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
